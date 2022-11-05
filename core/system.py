import helper,sys
global PYFRIEND_FRAME
def systemLoad(PYFRIEND_FRAME_M):
  PYFRIEND_FRAME = PYFRIEND_FRAME_M
  helper.PrintConsole("Welcome","Hello User","The system starts to load and run . ",1)
  helper.PrintConsole("Check","Vesion",PYFRIEND_FRAME["Init"]("PYFRIEND_INFO_VERSION"),1)
  return
