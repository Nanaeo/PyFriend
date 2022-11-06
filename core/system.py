import helper,sys,os
def loadPluginPackage(PYFRIEND_SYSTEM_TOKEN,pluginName):
    pluginPackage = "plugins." + pluginName
    authCode = helper.globalDict.authRegist(pluginName)
    authRange(authCode,pluginName)
    ip_module = importlib.import_module(pluginPackage)
    if helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","DEBUG"]):
      helper.PrintConsole("INFO","PLUGIN_LOAD",f"PLUGIN[{pluginName}] Package Loaded .",1)
    pluginClass = getattr(ip_module.Plugin, "Plugin")
    pluginInstance = pluginClass(authCode)   
    helper.GlobalDict.setValue(PYFRIEND_SYSTEM_TOKEN,[pluginName,"pluginInstance"],pluginInstance)   
def systemLoad(PYFRIEND_SYSTEM_TOKEN):
  helper.PrintConsole("Welcome","Hello User","The system starts to load and run . ",1)
  PYFRIEND_PATH_PLUGINS = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","PATH_PLUGINS"])
  PYFRIEND_SYSTEM_VERSION = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","VERSION"])
  helper.PrintConsole("System","Vesion",PYFRIEND_SYSTEM_VERSION,1)
  pluginsPath = os.listdir( PYFRIEND_PATH_PLUGINS ) 
  PluginBase = helper.PluginBase
  print(PluginBase)
  for pluginPathName in pluginsPath:
# 转入Plugin类加载所有插件 然后公布绑定事件 分析触发事件运行流程     
    PluginBase.LoadPlugin(PYFRIEND_SYSTEM_TOKEN,pluginsPath,pluginPathName)
    loadPluginPackage(PYFRIEND_SYSTEM_TOKEN,pluginPathName)
  t = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["Builder","CONFIG"])
  print(t)
  return
