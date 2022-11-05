import helper,sys
def systemLoad(PYFRIEND_SYSTEM_TOKEN):
  helper.PrintConsole("Welcome","Hello User","The system starts to load and run . ",1)
  PYFRIEND_SYSTEM_VERSION = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","VERSION"])
  helper.PrintConsole("System","Vesion",PYFRIEND_SYSTEM_VERSION,1)
  return
