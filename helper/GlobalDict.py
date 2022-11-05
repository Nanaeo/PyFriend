import uuid
# 初始化获取顶级权限
def _init():
  global _global_dict
  global rootCode
  authTable = {}
  _global_dict = {}
  rootCode = str(uuid.uuid4())
  authTable[rootCode] = {"name":"system","auth":1,"range":{}} 
  return rootCode
def set_value(authCode , key, value):
  if rootCode in authTable:
    tempdata = _global_dict
    if not key[0] in authTable[rootCode]["range"]:
       return False
    for temp in key:
       tempdata = tempdata[temp]
    return True
  else:
    return False
def get_value(authCode,key):
  if rootCode in authTable:
  tempdata = _global_dict
  if not key[0] in authTable[rootCode]["range"]:
    return False
  for temp in key:
     tempdata = tempdata[temp]
  return tempdata
