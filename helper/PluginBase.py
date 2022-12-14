import os, sys
import yaml,importlib
import helper
class PluginBase(object):
  def LoadPlugin(PYFRIEND_SYSTEM_TOKEN,pluginsPath,pluginPathName):
    PYFRIEND_PATH_PLUGINS = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","PATH_PLUGINS"])
    pluginPath = f"{PYFRIEND_PATH_PLUGINS}//{pluginPathName}"
    if os.path.isdir(pluginPath):
      if os.path.exists(f"{pluginPath}//{pluginPathName}.plugin.yml"):
        pluginConfigFile = open(f"{pluginPath}//{pluginPathName}.plugin.yml","r") 
        pluginConfig = yaml.load(pluginConfigFile.read(),Loader=yaml.FullLoader)
        if os.path.exists(f"{pluginPath}//Plugin.py"):        
          if "pluginName" in pluginConfig :
            pluginName = pluginConfig["pluginName"]
            helper.GlobalDict.setValue(PYFRIEND_SYSTEM_TOKEN,[pluginPathName,"CONFIG"],pluginConfig)
            helper.PrintConsole("INFO","PLUGIN_LOAD",f"PLUGIN[{pluginName}] Basic Info Loaded .",1)  
          else: 
            helper.PrintConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] .")  
        else: 
          helper.PrintConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , the feature implementation section was not found.",0)  
        pluginConfigFile.close()  
      else:
        helper.PrintConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , No configuration information was found.",0)
