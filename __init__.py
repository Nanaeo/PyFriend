# PyFriend Load Helper
import os,sys,traceback
from helper import PyFriendException
import core,helper 
# Common variable
PYFRIEND_INFO_VERSION = "1.0.0"
PYFRIEND_CONFIG_DEBUG = True
# Machine generated
PYFRIEND_PATH_ROOT = os.path.abspath(os.path.dirname(__file__))
PYFRIEND_PATH_PLUGINS = PYFRIEND_PATH_ROOT + "//plugins"
# Reference PYFRIEND_PATH_ROOT https://www.cnblogs.com/liangmingshen/p/12794631.html
try:
  if(__name__=="__main__"):
    core.systemLoad()
except Exception as e:
  errorMsg = traceback.format_exc()
  helper.PrintConsole("FATAL","SYSTEM",f"Specific information :\n {errorMsg}")
except PyFriendException as e:
  helper.PrintConsole(e.Type,e.Location,e.Msg,e.Color)
