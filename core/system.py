import helper,sys,os
def systemLoad(PYFRIEND_SYSTEM_TOKEN):
  helper.PrintConsole("Welcome","Hello User","The system starts to load and run . ",1)
  PYFRIEND_PATH_PLUGINS = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","PATH_PLUGINS"])
  PYFRIEND_SYSTEM_VERSION = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","VERSION"])
  helper.PrintConsole("System","Vesion",PYFRIEND_SYSTEM_VERSION,1)
  pluginsPath = os.listdir( PYFRIEND_PATH_PLUGINS ) 
  for pluginPathName in pluginsPath:
# 转入Plugin类加载所有插件 然后公布绑定事件 分析触发事件运行流程
      helper.PluginBase.LoadPlugin(PYFRIEND_SYSTEM_TOKEN,pluginsPath,pluginPathName)
  t = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["Builder","CONFIG"])
  print(t)
  return
