from iocbuilder import AutoSubstitution
from iocbuilder.arginfo import *
from iocbuilder.modules.calc import Calc
from iocbuilder.modules.busy import Busy

class multipositioner(AutoSubstitution):
    Dependencies = (Calc,Busy)
    # Substitution attributes
    TemplateFile = 'multipositioner.template'
    
    def addPositioner(self, Q):
        # register a positioner object with this
        if "positioners" not in self.__dict__:
            self.positioners = []    
        assert Q not in self.positioners, \
        	"Positioner %s already added to %s" % (Q, self.args["P"])
        self.positioners.append(Q)
        return chr(64+len(self.positioners))

    def Finalise(self):
        # create the args needed for the gui
        self.args["NPOS"] = len(self.positioners)
        for i, q in enumerate(self.positioners):
            self.args["P%d"%(i+1)]= q.args["Q"]

class _motorpositionerTemplate(AutoSubstitution):
    # Substitution attributes
    TemplateFile = 'motorpositioner.template'

try:
    from iocbuilder.modules.motor import MotorRecord

    # this is a motorpositioner object
    class motorpositioner(_motorpositionerTemplate):
        __doc__ = _motorpositionerTemplate.__doc__
        def __init__(self, MP, motor, **args):
            # get PV prefixes from parent
            args['P'], args['MP'] = MP.args['P'], MP.args['MP']
            # register as multipositioner object
            args['pos'] = MP.addPositioner(self)
            # strip out the motor record pv and egu from the object
            assert motor.args['P'] == args['P'], \
                "Motor prefix must match motor positioner prefix"
            args['motor'] = motor.args['M']
            args['EGU'] = motor.args['EGU']
            self.__super.__init__(**args)
            
        # construct the ArgInfo        
        ArgInfo = makeArgInfo(__init__,
            MP    = Ident('Parent multipositioner object', multipositioner),
            motor = Ident('Motor record object', MotorRecord)) + \
            _motorpositionerTemplate.ArgInfo.filtered(
                without = ('P', 'MP', 'pos', 'motor', 'EGU'))        

except ImportError:
    print "# motor not included, cannot make motorpositioner object"             
                                                                        
class _positionerTemplate(AutoSubstitution):
    # Substitution attributes
    TemplateFile = 'positioner.template'

# this is a positioner object
class positioner(_positionerTemplate):
    __doc__ = _positionerTemplate.__doc__
    def __init__(self, MP, **args):
        # get PV prefixes from parent
        args['P'], args['MP'] = MP.args['P'], MP.args['MP']
        # register as multipositioner object
        args['pos'] = MP.addPositioner(self)
        self.__super.__init__(**args)
        
    # construct the ArgInfo        
    ArgInfo = makeArgInfo(__init__,
        MP = Ident('Parent multipositioner object', multipositioner)) + \
        _positionerTemplate.ArgInfo.filtered(without = ('P', 'MP', 'pos'))        
