TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

DBD += positioner_vdct.dbd
# positioner.dbd will be made up from these files:
positioner_vdct_DBD += base.dbd
positioner_vdct_DBD += transformRecord.dbd
positioner_vdct_DBD += busyRecord.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
positioner_SRCS += positioner_registerRecordDeviceDriver.cpp
positioner_SRCS_DEFAULT += positionerMain.cpp
positioner_SRCS_vxWorks += -nil-

#The following adds support from base/src/vxWorks
positioner_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
#positioner_LIBS += xxx

positioner_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

