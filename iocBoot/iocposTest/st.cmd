#!../../bin/linux-x86/posTest

## You may have to change posTest to something else
## everywhere it appears in this file

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/posTest.dbd",0,0)
posTest_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/posTest.db")

# Configure simulation PMAC
var simulation_mode 1
PmacSetup(1,0,0,0,0,0,10)

cd ${TOP}/iocBoot/${IOC}
iocInit()

## Start any sequence programs
#seq sncxxx,"user=mw23Host"
