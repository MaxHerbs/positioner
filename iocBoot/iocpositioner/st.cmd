#!../../bin/linux-x86/positioner

## You may have to change positioner to something else
## everywhere it appears in this file

epicsEnvSet(EPICS_CA_REPEATER_PORT,"6065")
epicsEnvSet(EPICS_CA_SERVER_PORT,"6064")

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/positioner.dbd",0,0)
positioner_registerRecordDeviceDriver(pdbbase)

## Load record instances
#dbLoadRecords("db/example.db","user=pjl45")
cd db
dbLoadTemplate("$(TOP)/example/example.substitutions","user=pjl45")
#dbLoadRecords("$(TOP)/example/example_support.db","user=pjl45")

# Configure simulation PMAC
var simulation_mode 1
PmacSetup(1,0,0,0,0,0,0)

cd ${TOP}/iocBoot/${IOC}
iocInit()

## Start any sequence programs
#seq sncxxx,"user=pjl45Host"
