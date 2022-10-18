# PyFriend
基于GithubAction的自动化友情链接管理
# 目录结构
```
PyFriend
│   README.md
│   core.py  
│   plugin.py  
│
└───plugin
│   │   LightHouseTest.py
│   │   Test.py
│   │   install.py
│   │   ...
│   
└───config
│   │  config.yml
│   │  event.config.yml
│   │  Test.config.yml
│   │  plugin.config.yml
│   │   ...
│
└───script
│   │  LightHouseTest.test.sh
│   │   ...
│
```
# 工作过程
1.修改 plugin.config.yml 将会自动启动 Action 刷新event注册表.

2. Github修改监听文件和github事件调用Action,Action启动时加载Plugin,并通过 plugin.config.yml 配置获取插件已经注册的event.

通过已经约定的插件event注册表,调用插件处理.
