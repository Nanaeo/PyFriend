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
  global authTable
  authTable = {}
  globalDict = {}
  rootCode = str(uuid.uuid4())
  authTable[rootCode] = {"name":"system","auth":1,"range":{}} 
  return rootCode

def authRegist(name):
   authCode = str(uuid.uuid4())
   authTable[authCode] = {"name":name,"auth":0,"range":{name:"1"}} 

def authRange(authCode,key):
  if not authCode in authTable:
    return False
  if authTable[authCode]["auth"] == 0:
    return False
  authTable[authCode]["range"][key] = 1

def setValue(authCode , keys, value):
  if not authCode in authTable:
    return False
  if not keys[0] in authTable[authCode]["range"] and authTable[authCode]["auth"] == 0:
    return False
  us(globalDict,keys,value)
  return True

def getValue(authCode,keys):
  print(authTable)
  if not authCode in authTable:
    return False
  if not keys[0] in authTable[authCode]["range"] and authTable[authCode]["auth"] == 0:
    return False
  tempdata = globalDict
#  print(tempdata)
  for temp in keys:
     tempdata = tempdata[temp]
  return tempdata
