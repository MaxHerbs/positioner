from iocbuilder import Substitution
from iocbuilder.arginfo import *
from iocbuilder.modules.calc import Calc


class multipositioner(Substitution):
    '''A brief description for this class goes here'''
    Dependencies = (Calc,)

    # The __init__ method specifies arguments and defaults
    def __init__(self, P, MP, DESC, STRS = [''], name = '', gda = True):
        # If gda then define gda_name and gda_desc
        if gda:
            gda_name, gda_desc = name, DESC
        else:
            gda_name, gda_desc = '', ''
        # set strs to defaults
        for v,x in zip(self._strs, STRS + [""] * 12):
            locals()[v] = x          
        self.positioners = []
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(NPOS = 0, **filter_dict(locals(), self.Arguments))

    def addPositioner(self, Q):
        assert Q not in self.positioners, "Positioner %s already added to %s" % (Q, self.args["P"])
        self.positioners.append(Q)
        return chr(64+len(self.positioners))
        
    def Finalise(self):
        self.args["NPOS"] = len(self.positioners)
        for i, q in enumerate(self.positioners):
            self.Arguments.append("P%d"%(i+1))
            self.args["P%d"%(i+1)]= q

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        P    = Simple('PV prefix', str),
        MP   = Simple('PV suffix', str),
        DESC = Simple('Object description, also used for gda_desc if gda', str),
        STRS = List  ('Position Labels', 12, Simple, str),
        name = Simple('Object name, also used for gda_name if gda', str),
        gda  = Simple('Set to True to make available to gda', bool))

    # Substitution attributes
    TemplateFile = 'multipositioner.template'
    _strs = ["STR%s" % chr(65+i) for i in range(12)]    
    Arguments = ArgInfo.Names(without = ["STRS"]) + _strs + ["NPOS", "gda_name", "gda_desc"]


class _positionerBase(Substitution):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, MP, Q, DESC, VALS = [0.0], PREC = 4, EGU="mm", **args):    
        # check positioner number is ok
        pos = MP.addPositioner(Q)        
        # grab P and MP from multipositioner
        P = MP.args["P"]
        MP = MP.args["MP"]
        # set vals to defaults
        for v,x in zip(self._vals, VALS + [0.0] * 12):
            locals()[v] = x
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        locals().update(args)        
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    _ArgInfo = makeArgInfo(__init__,
        MP    = Ident ('Multipositioner object', multipositioner),
        Q     = Simple('Positioner suffix', str),
        DESC  = Simple('Positioner description', str),
        PREC  = Simple('Display Precision', int),
        EGU   = Simple('Display Engineering Units', str),
        VALS  = List  ('Motor positions', 12, Simple, float))

    # Substitution attributes
    _vals = ["VAL%s" % chr(65+i) for i in range(12)]
    Arguments = ["P", "pos"] + _ArgInfo.Names(without = ["VALS"]) + _vals

try:
    from iocbuilder.modules.motor import basic_asyn_motor
    
    class motorpositioner(_positionerBase):
        '''Positioner that wraps a motor record'''

        # The __init__ method specifies arguments and defaults
        def __init__(self, motor, **args):
            # Grab the motor record name from the motor object
            motor = motor.args["P"] + motor.args["M"]
            assert motor.startswith(args["MP"].args["P"]), "Motor record must have the same prefix as multipositioner object"
            motor = motor[len(args["MP"].args["P"]):]
            # Filter the list of local variables by the argument list,
            # then initialise the super class
            args.update(locals())
            args.pop("self")
            self.__super.__init__(**args)

        # __init__ arguments
        ArgInfo = _positionerBase._ArgInfo + makeArgInfo(__init__,
            motor = Ident ('Motor object', basic_asyn_motor))

        # Substitution attributes
        TemplateFile = 'motorpositioner.template'
        Arguments = ["motor"] + _positionerBase.Arguments    
        
except ImportError, e:
    pass

class positioner(_positionerBase):
    '''Positioner that wraps a motor record'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, READBACK, SET, DEADBAND, STOP, STOPVAL, **args):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        args.update(locals())
        args.pop("self")
        self.__super.__init__(**args)

    # __init__ arguments
    ArgInfo = _positionerBase._ArgInfo + makeArgInfo(__init__,
        READBACK = Simple('Readback Positioner Pv = $(MP.P)$(READBACK)', str),
        SET      = Simple('Set Positioner Pv = $(MP.P)$(READBACK)', str),
        DEADBAND = Simple('Deadband allowable between Readback and Set', float),
        STOP     = Simple('Stop Positioner Pv = $(MP.P)$(READBACK)', str),
        STOPVAL  = Simple('Value to send on stop', str))

    # Substitution attributes
    TemplateFile = 'positioner.template'
    Arguments = ['READBACK', 'SET', 'DEADBAND', 'STOP', 'STOPVAL'] + \
        _positionerBase.Arguments    

