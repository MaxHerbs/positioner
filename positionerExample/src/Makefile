TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

PROD_IOC = posTest

DBD += posTest.dbd
# posTest.dbd will be made up from these files:
posTest_DBD += base.dbd
posTest_DBD += motorSupport.dbd
posTest_DBD += devSoftMotor.dbd
posTest_DBD += devDeltaTau.dbd
posTest_DBD += positioner.dbd
#include definitions for any other support applications needed
#posTest_DBD += xxx.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
posTest_SRCS += posTest_registerRecordDeviceDriver.cpp
posTest_SRCS_DEFAULT += posTestMain.cpp
posTest_SRCS_vxWorks += -nil-

#The following adds support from base/src/vxWorks
posTest_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
#posTest_LIBS += xxx

#NOTES:
#      1)It is not possible to build sncExample both as a component of posTest
#        and standalone. You must choose only one.
#      2)To build sncExample SNCSEQ must be defined in <top>/configure/RELEASE

#The following builds sncExample as a component of posTest
#posTest_SRCS += sncExample.stt
#posTest_LIBS += seq pv

posTest_LIBS += softMotor
posTest_LIBS += DeltaTau
posTest_LIBS += calc
posTest_LIBS += positioner

posTest_LIBS += $(EPICS_BASE_IOC_LIBS)

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

