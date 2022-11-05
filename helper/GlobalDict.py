import uuid
# 初始化获取顶级权限 不完善
def us(di,keys,val):
    length = len(keys)
    if(length == 0):
        return val
    else:
        key = keys.pop(0)
        if(key in di.keys()):
            di[key] = us(di[key],keys,val)
        else:
            di[key] = us({},keys,val)
        return di

def authInit():
  global globalDict
  global rootCode
  authTable = {}
  globalDict = {}
  rootCode = str(uuid.uuid4())
  authTable[rootCode] = {"name":"system","auth":1,"range":{}} 
  return rootCode

def authRegist(name):
   rootCode = str(uuid.uuid4())
   authTable[rootCode] = {"name":name,"auth":0,"range":{name:"3"}} 

def setValue(authCode , keys, value):
  if not rootCode in authTable:
    return False
  if not keys[0] in authTable[rootCode]["range"] and authTable[rootCode]["auth"] != 0:
    return False
  globalDict = us(globalDict,keys,value)
  return True

def getValue(authCode,keys):
  if not rootCode in authTable:
    return False
  if not key[0] in authTable[rootCode]["range"] and authTable[rootCode]["auth"] != 0:
    return False
  tempdata = globalDict
  for temp in keys:
     tempdata = tempdata[temp]
  return tempdata
