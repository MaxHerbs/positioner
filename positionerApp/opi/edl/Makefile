TOP = ../../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

# The following are used for debugging messages.
DATA += $(patsubst ../%, %, $(wildcard ../*.edl))
DATA += $(patsubst ../%, %, $(wildcard ../*.gif))
DATA += $(patsubst ../%, %, $(wildcard ../*.png))

include $(TOP)/configure/RULES
