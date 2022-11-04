# PyFriends
基于GithubAction的自动化友情链接管理
# 目录结构
```
PyFriend
│   README.md
│   core.py  
│   plugin.py  
│
└───plugins
│   │   LightHouseTest
│   │   Test
│   │   install
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
# 设计方案
<details><summary>Event表?</summary><br>
event注册表是插件需要工作所必须的,是记录插件何时被调用与如何工作的文件
/config/plugin.config.yml 就是event表的储存文件
</details>
<details><summary>插件注册Event表</summary><br>
修改 plugin.config.yml 将会自动启动 Action 刷新event注册表.
</details>
<details><summary>执行功能</summary><br>
Github修改监听文件和github事件调用Action,Action启动时加载Plugin,并通过 plugin.config.yml 配置获取插件已经注册的event.
通过已经约定的插件event注册表,调用插件处理
</details>

# 计划
- [ ] 插件系统

- [ ] 插件系统

- [ ] 插件系统

- [ ] 插件系统
