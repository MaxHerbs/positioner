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
#DB += xxx.db

DB += positioner.template
DB += position.template
# VDCT definitions
#VDB_DEPS += xxx.vdb yyy.vdb

#DB += $(TOP)/example/example.db

#USES_TEMPLATE += $(TOP)/db/positioner.template
#USES_TEMPLATE += $(TOP)/db/position.template

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

