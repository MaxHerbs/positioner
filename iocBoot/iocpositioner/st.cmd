#!../../bin/linux-x86/positioner

## You may have to change positioner to something else
## everywhere it appears in this file

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/positioner.dbd",0,0)
positioner_registerRecordDeviceDriver(pdbbase)

## Load record instances
#dbLoadRecords("db/xxx.db","user=pjl45Host")

cd ${TOP}/iocBoot/${IOC}
iocInit()

## Start any sequence programs
#seq sncxxx,"user=pjl45Host"
