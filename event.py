#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys,traceback
import yaml
import importlib
from colorama import init, Fore, Back, Style

PYFRIEND_INFO_VERSION = "1.0.0"
PYFRIEND_CONFIG_DEBUG = True
PYFRIEND_PATH_ROOT = os.path.abspath(os.path.dirname(__file__))
PYFRIEND_PATH_PLUGINS = PYFRIEND_PATH_ROOT + "//plugins"
# Reference PYFRIEND_PATH_ROOT https://www.cnblogs.com/liangmingshen/p/12794631.html

PYFRIEND_CONFIG_PLUGINS = {}
PYFRIEND_INFO_PLUGINS = {}
PYFRIEND_CLASS_PLUGINS = {}
PYFRIEND_EVENT_BIND = {}
PYFRIEND_INSTANCE_PLUGINS ={}
PYFRIEND_EVENT_REGISTER = {}
# Inital Plugins Table
def infoConsole(Type,Location,Msg,Color = 0):
  output = f"[{Type}]" + Fore.RESET + f"[{Location}] {Msg}"
  if  Color  == 0:
    print(Fore.RED + output)
  elif Color == 1:
    print(Fore.GREEN + output)
  else:
    print(Fore.YELLOW + output)
  return
# Yaml will be fully loaded in Full unsafe mode
def systemLoad():
  loadPluginInfo()
  loadPluginPackage()
def loadPluginInfo():  
  pluginsPath = os.listdir( PYFRIEND_PATH_PLUGINS ) 
  for pluginPathName in pluginsPath:
    pluginPath = f"{PYFRIEND_PATH_PLUGINS}//{pluginPathName}"
    if os.path.isdir(pluginPath):
      if os.path.exists(f"{pluginPath}//{pluginPathName}.plugin.yml"):
        pluginConfigFile = open(f"{pluginPath}//{pluginPathName}.plugin.yml","r")   
        pluginConfig = yaml.load(pluginConfigFile.read(),Loader=yaml.FullLoader)
        if os.path.exists(f"{pluginPath}//Plugin.py"):        
          if "pluginName" in pluginConfig and pluginConfig["pluginName"] == pluginPathName:
            pluginName = pluginConfig["pluginName"]
            PYFRIEND_CONFIG_PLUGINS[pluginName] = pluginConfig  
            PYFRIEND_CONFIG_PLUGINS[pluginName]["EntryFile"] = f"{pluginPath}//Plugin.py"
            infoConsole("INFO","PLUGIN_LOAD",f"PLUGIN[{pluginName}] Basic Info Loaded .",1)  
          else: 
            infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] .")  
        else: 
          infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , the feature implementation section was not found.")  
      else:
        infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , No configuration information was found.")
def loadPluginPackage():
  for pluginIndex in PYFRIEND_CONFIG_PLUGINS:
    pluginName = PYFRIEND_CONFIG_PLUGINS[pluginIndex]["pluginName"]
    pluginPackage = "plugins." + pluginName
    ip_module = importlib.import_module(pluginPackage)
    if PYFRIEND_CONFIG_DEBUG:
      infoConsole("INFO","PLUGIN_LOAD",f"PLUGIN[{pluginName}] Package Loaded .",1)
     PYFRIEND_CLASS_PLUGINS[pluginName] = getattr(ip_module, "Plugin")
#    PYFRIEND_INSTANCE_PLUGINS[pluginName] = PYFRIEND_CLASS_PLUGINS[pluginName](1000)
if(__name__=="__main__"):
  try:
    systemLoad()
    print(PYFRIEND_CLASS_PLUGINS)
    print("类型：", type(PYFRIEND_CLASS_PLUGINS))
  except Exception as e:
    errorMsg = traceback.format_exc()
    infoConsole("FATAL","OTHER",f"SYSTEM[CAPTRUE] Specific information :\n {errorMsg}")
