import helper,sys
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
      pluginConfigFile.close()  
      else: 
        helper.PrintConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , the feature implementation section was not found.",0)  
    else:
      helper.PrintConsole("ERROR","PLUGIN_LOAD",f"PLUGIN[{pluginPathName}] Unable to load properly , No configuration information was found.",0)
def systemLoad(PYFRIEND_SYSTEM_TOKEN):
  helper.PrintConsole("Welcome","Hello User","The system starts to load and run . ",1)
  PYFRIEND_PATH_PLUGINS = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","PATH_PLUGINS"])
  PYFRIEND_SYSTEM_VERSION = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["SYSTEM","VERSION"])
  helper.PrintConsole("System","Vesion",PYFRIEND_SYSTEM_VERSION,1)
  pluginsPath = os.listdir( PYFRIEND_PATH_PLUGINS ) 
  for pluginPathName in pluginsPath:
# 转入Plugin类加载所有插件 然后公布绑定事件 分析触发事件运行流程
      LoadPlugin(PYFRIEND_SYSTEM_TOKEN,pluginsPath,pluginPathName)
  t = helper.GlobalDict.getValue(PYFRIEND_SYSTEM_TOKEN,["Builer","CONFIG"])
  print(t)
  return
