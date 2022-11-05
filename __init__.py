# PyFriend Load Helper
import os,sys,traceback 
from helper import PyFriendException
import core,helper 
# Common variable
# None
# Machine generated
PYFRIEND_PATH_ROOT = os.path.abspath(os.path.dirname(__file__))
PYFRIEND_PATH_PLUGINS = PYFRIEND_PATH_ROOT + "//plugins"
# Reference PYFRIEND_PATH_ROOT https://www.cnblogs.com/liangmingshen/p/12794631.html
def getVar(name):
  return sys._getframe().f_back.f_locals[name]
try:
  if(__name__=="__main__"):      
    PYFRIEND_SYSTEM_TOKEN = helper.GlobalDict.authInit()
    helper.GlobalDict.setValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","VERSION"],"1.0.0")
    helper.GlobalDict.setValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","DEBUG"],True)
    helper.GlobalDict.setValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","PATH_ROOT"],os.path.abspath(os.path.dirname(__file__)))
    helper.GlobalDict.setValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","PATH_PLUGINS"],os.path.abspath(os.path.dirname(__file__)) + "//plugins")
    core.systemLoad(PYFRIEND_SYSTEM_TOKEN)
except Exception as e:
  errorMsg = traceback.format_exc()
  helper.PrintConsole("FATAL","SYSTEM",f"Specific information :\n {errorMsg}")
except PyFriendException as e:
  helper.PrintConsole(e.Type,e.Location,e.Msg,e.Color)

