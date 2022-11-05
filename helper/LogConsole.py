import time,sys,os
def PrintConsole(Type,Location,Msg,Color = 0):
  nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  output = f"[{Type}]" + Fore.RESET + f"[{nowtime}]{Location} : {Msg}"
  if  Color  == 0:
    print(Fore.RED + output)
  elif Color == 1:
    print(Fore.GREEN + output)
  else:
    print(Fore.YELLOW + output)
  return
