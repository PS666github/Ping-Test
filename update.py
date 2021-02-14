#!/usr/bin/python3
# This code write by (ms.nope)
import os
import time
os.system("clear")
print("""

▀█▀ █▀▀ █▀ ▀█▀ █░█░█ █▀▀ █▄▄
░█░ ██▄ ▄█ ░█░ ▀▄▀▄▀ ██▄ █▄█""")
time.sleep(1)
print("portscan update...")
os.system("cd ..")
os.system("sudo rm -r testweb/")
time.sleep(1)
os.system("cd ..") 
os.system("git clone https://github.com/msprogrammer2938/testweb.git")
time.sleep(1)
os.system("clear")
print("finish!")
time.sleep(1)
b = str(input("press Enter to run (testweb)... "))
if(str(b) == ''):
  os.system("cd testweb/")
time.sleep(1)
os.system("clear")
print("run testweb...")
time.sleep(1)
print("""
The installing finish i open directory (testweb) !
""")
time.sleep(4)
os.system("echo The packge upate in: ")
os.system("pwd")
t = str(input("Do you want to installing package? [y/n] "))
if(str(t) == 'y'):
  os.system("bash install.sh")
  w = str(input("Do you want run packge? [y/n] "))
  if(str(w) == 'y':
     os.system("python3 webtest.py")
  else:
      os.system("clear")
      print("good bye")
      exit(3)
if(str(t) == 'n'):
     os.system("clear")
     time.sleep(2)
     print("good bye")
     exit(1)
else:
    os.system("clear")
    time.sleep(1)
    print("Error 532 !")
    exit(1)
if(str(
exit(1)
# testweb
