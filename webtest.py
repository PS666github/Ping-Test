#!/usr/bin/python3
# This code write by ms.nope
import os
import time
class color:
    test = '\033[33m'
    white = '\033[0m'
os.system("clear")
print("""

    █───█ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ 
    █▄█▄█ █▀▀ █▀▀▄ ──█── █▀▀ ▀▀█ ──█── 
    ─▀─▀─ ▀▀▀ ▀▀▀─ ──▀── ▀▀▀ ▀▀▀ ──▀──
              (webtest)""")
print("1.Testweb")
print("2.Exit")
a = str(input("Test ~# "))
if(str(a) == '2'):
  os.system("clear")
  print("good bye")
  exit(1)
if(str(a) == '1'):
  os.system("clear")
  os.system("figlet webtest")
  ip = str(input("Enter ip: "))
  time.sleep(3)
  print(color.test)
  os.system("ping -w 2 " + ip)
  print(color.white)
  trygain = str(input("Do you want try again? [y/n] "))
  if(str(trygain) == 'y'):
    os.system("python3 webtest.py")
  if(str(trygain) == 'n'):
    os.system("clear")
    print("good bye")
    exit(1)
  else:
      os.system("clear") 	
      print("Error 532 !")
      Error = str(input("press Enter... "))
      if(str(Error) == ''):
        os.system("python3 webtest.py")
else:
    os.system("clear")
    print("Error 532 !")
    time.sleep(3)
    tryagain2 = str(input("press Enter... "))
    if(str(tryagain2) == ''):
      os.system("python3 webtest.py")
# webtest
