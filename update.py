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
exit(2)
# testweb
