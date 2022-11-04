#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

PYFRIEND_INFO_VERSION = "1.0.0"
PYFRIEND_SETTING_DEBUG = true
PYFRIEND_PATH_ROOT = os.path.abspath(os.path.dirname(__file__))
PYFRIEND_PATH_PLUGINS = PYFRIEND_PATH_ROOT + "/plugins"
# Reference PYFRIEND_PATH_ROOT https://www.cnblogs.com/liangmingshen/p/12794631.html

if(__name__=="__main__"):
  systemLoad()
def systemLoad():
  pluginsPath = os.listdir( PYFRIEND_PATH_PLUGINS ) 
  for file in pluginsPath:
    print(file)
