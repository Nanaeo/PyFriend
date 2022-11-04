#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

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
def infoConsole(Type,Location,Msg):
  print('[{0}][{1}] {2}'.format(Type,Location,Msg))
  return
def systemLoad():  
  pluginsPath = os.listdir( PYFRIEND_PATH_PLUGINS ) 
  for pluginName in pluginsPath:
    pluginPath = f"{PYFRIEND_PATH_PLUGINS}//{pluginName}"
    if os.path.isdir(pluginPath):
      if os.path.exists(f"{pluginPath}//{pluginName}.plugin.yml"):
        pluginConfig = open(f"{pluginPath}//{pluginName}.plugin.yml","r")   
        print(pluginConfig.read())
      else:
        infoConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginName}] Unable to load properly.")
if(__name__=="__main__"):
  systemLoad()
