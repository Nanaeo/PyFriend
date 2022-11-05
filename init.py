#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys,traceback
from colorama import init, Fore, Back, Style
import yaml

PYFRIEND_INFO_VERSION = "1.0.0"
PYFRIEND_CONFIG_DEBUG = True
PYFRIEND_PATH_ROOT = os.path.abspath(os.path.dirname(__file__))
PYFRIEND_PATH_PLUGINS = PYFRIEND_PATH_ROOT + "//plugins"
# Reference PYFRIEND_PATH_ROOT https://www.cnblogs.com/liangmingshen/p/12794631.html

PYFRIEND_CONFIG_PLUGINS = {}
PYFRIEND_INFO_PLUGINS = {}
PYFRIEND_EVENT_BIND = {}
PYFRIEND_EVENT_REGISTER = {}
# Inital Plugins Table
def infoConsole(Type,Location,Msg,color = 0):
  output = f"[{Type}]" + Fore.RESET + f"[{Location}] {Msg}"
  if  color  == 0:
    print(Fore.RED + output)
  elif color == 1:
    print(Fore.GREEN + output)
  else:
    print(Fore.YELLOW + output)
  return
# Yaml will be fully loaded in Full unsafe mode
def systemLoad():  
  pluginsPath = os.listdir( PYFRIEND_PATH_PLUGINS ) 
  for pluginPathName in pluginsPath:
    pluginPath = f"{PYFRIEND_PATH_PLUGINS}//{pluginPathName}"
    if os.path.isdir(pluginPath):
      if os.path.exists(f"{pluginPath}//{pluginPathName}.plugin.yml"):
        pluginConfigFile = open(f"{pluginPath}//{pluginPathName}.plugin.yml","r")   
        pluginConfig = yaml.load(pluginConfigFile.read(),Loader=yaml.FullLoader)
        if os.path.exists(f"{pluginPath}//plugin.py"):
          print(pluginConfig)
          if "pluginName" in pluginConfig and pluginConfig.pluginName == pluginPathName:
            pluginName = pluginConfig.pluginName
            PYFRIEND_CONFIG_PLUGINS[pluginConfig.pluginName] = pluginConfig  
            infoConsole("INFO","PLUGIN_LOAD",f"PLUGIN[{pluginName}] begins to load .")  
          else: 
            infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] .",1)  
        else: 
          infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , the feature implementation section was not found.")  
      else:
        infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , No configuration information was found.")
if(__name__=="__main__"):
  try:
    systemLoad()
    print(PYFRIEND_CONFIG_PLUGINS)
    print("类型：", type(PYFRIEND_CONFIG_PLUGINS))
  except Exception as e:
    errorMsg = traceback.format_exc()
    infoConsole("FATAL","OTHER",f"SYSTEM[CAPTRUE] Specific information :\n {errorMsg}")
