TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

PROD_IOC_Linux = positioner

DBD += positioner.dbd
# positioner.dbd will be made up from these files:
positioner_DBD += base.dbd
#include definitions for any other support applications needed
#positioner_DBD += xxx.dbd
positioner_DBD += motorSupport.dbd
positioner_DBD += devSoftMotor.dbd
positioner_DBD += devDeltaTau.dbd


# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
positioner_SRCS += positioner_registerRecordDeviceDriver.cpp
positioner_SRCS_DEFAULT += positionerMain.cpp
positioner_SRCS_vxWorks += -nil-

#The following adds support from base/src/vxWorks
positioner_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
#positioner_LIBS += xxx

#NOTES:
#      1)It is not possible to build sncExample both as a component of positioner
#        and standalone. You must choose only one.
#      2)To build sncExample SNCSEQ must be defined in <top>/configure/RELEASE

#The following builds sncExample as a component of positioner
#positioner_SRCS += sncExample.stt
#positioner_LIBS += seq pv

positioner_LIBS += $(EPICS_BASE_IOC_LIBS)
positioner_LIBS += motor
positioner_LIBS += softMotor
positioner_LIBS += DeltaTau

#The following builds sncExample as a standalone application
#PROD_HOST += sncExample
#sncExample_SNCFLAGS += +m
#sncExample_SRCS += sncExample.stt
#sncExample_LIBS += seq pv
#sncExample_LIBS += $(EPICS_BASE_HOST_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

