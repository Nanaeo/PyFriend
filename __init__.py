# PyFriend Load Helper
from helper import *
from . import system
# Common variable
PYFRIEND_INFO_VERSION = "1.0.0"
PYFRIEND_CONFIG_DEBUG = True
# Machine generated
PYFRIEND_PATH_ROOT = os.path.abspath(os.path.dirname(__file__))
PYFRIEND_PATH_PLUGINS = PYFRIEND_PATH_ROOT + "//plugins"
# Reference PYFRIEND_PATH_ROOT https://www.cnblogs.com/liangmingshen/p/12794631.html
try:
  if(__name__=="__main__"):
    systemLoad()
except PyFriendException as e:
  errorMsg = traceback.format_exc()
  infoConsole("FATAL","SYSTEM",f"Specific information :\n {errorMsg}")
except Exception as e:
  infoConsole(e.Type,e.Location,e.Msg,e.Color)
