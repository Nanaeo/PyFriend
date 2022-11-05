import os, sys
import yaml
import importlib
class PluginBase(object):
  Plugins = {}
  def LoadPlugin(PluginPath,pluginFileName):      
    if os.path.isdir(pluginPath):
      if os.path.exists(f"{pluginPath}//{pluginFileName}.plugin.yml"):
        pluginConfigFile = open(f"{pluginPath}//{pluginFileName}.plugin.yml","r")   
        pluginConfig = yaml.load(pluginConfigFile.read(),Loader=yaml.FullLoader)
        pluginConfigFile.close()
        if os.path.exists(f"{pluginPath}//Plugin.py"):        
          if "pluginName" in pluginConfig:
            pluginName = pluginConfig["pluginName"]
            Plugins["config"][pluginName] = pluginConfig  
            Plugins["config"][pluginName]["packageName"] = f"plugins.{pluginName}"
            infoConsole("INFO","PLUGIN_LOAD",f"PLUGIN[{pluginName}] Basic Info Loaded .",1)  
          else: 
            infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] .")  
        else: 
          infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , the feature implementation section was not found.")  
      else:
        infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , No configuration information was found.")
