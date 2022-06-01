W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		
		print ("""\033[1;92m
		
		
 /$$$$$$$  /$$$$$$ /$$      /$$  /$$$$$$  /$$   /$$
| $$__  $$|_  $$_/| $$$    /$$$ /$$__  $$| $$$ | $$
| $$  \ $$  | $$  | $$$$  /$$$$| $$  \ $$| $$$$| $$
| $$$$$$$/  | $$  | $$ $$/$$ $$| $$  | $$| $$ $$ $$
| $$__  $$  | $$  | $$  $$$| $$| $$  | $$| $$  $$$$
| $$  \ $$  | $$  | $$\  $ | $$| $$  | $$| $$\  $$$
| $$  | $$ /$$$$$$| $$ \/  | $$|  $$$$$$/| $$ \  $$
|__/  |__/|______/|__/     |__/ \______/ |__/  \__/


\033[1;90m══════════════════════════════════════════════════
\033[1;91m [\033[1;97m◆\033[1;91m] \033[1;93mFACEBOOK : BLACK-BOY 
\033[1;91m [\033[1;97m◆\033[1;91m] \033[1;92mFB GROUP : BLACK-BOY 
\033[1;91m [\033[1;97m◆\033[1;91m] \033[1;96mGITHUB   : Black-Boy
\033[1;91m [\033[1;97m◆\033[1;91m] \033[1;91mAUTHOR   : RIMON-KHAN 
\033[1;90m══════════════════════════════════════════════════
    """)
       
		print(" \n\033[1;92m     FUCK NAIM 🖕🖕🖕   ")
		print("")
		print("%s [%s1%s]%s FUCK BYPASS (Naim75o) %s"%(G,R,G,W,B))
		print("%s [%s2%s]%s EXIT %s"%(G,R,G,W,B))
		print("")
		rimon = input(" \033[0;91m[!]\033[0;92m CHOOSE : ")
		print("")
		if rimon in ["", " "]:
			Main()
		elif rimon in ["1", "01"]:
				    os.system("rm -rf FUCK-NAIM")
				    os.system("git clone https://github.com/BlackBoy26/FUCK-NAIM")
				    os.system("cd FUCK-NAIM")
				    os.system("python3 dad1.py")
		elif rimon in ["2", "02"]:
		    Main()

try:Main()
except Exception as e:exit(str(e))