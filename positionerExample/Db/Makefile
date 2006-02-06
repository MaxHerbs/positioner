TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install) into <top>/db
# databases, templates, substitutions like this
DB += posTest.db

USES_TEMPLATE += $(POSITIONER)/db/multipositioner.template
USES_TEMPLATE += $(POSITIONER)/db/motorpositioner.template
USES_TEMPLATE += $(POSITIONER)/db/positioner.template
USES_TEMPLATE += $(MOTOR)/db/basic_motor.template

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

-include $(TOP)/configure/RULES.Db
include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

