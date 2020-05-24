import socket
import time
from colorama import init, Fore
init()
RESET = Fore.RESET
GREEN = Fore.GREEN
print ("This scan can take a very long time !")
time.sleep(1)
host = input("[+]Target ip : ")
num = int(input("How many ports do you want to test for : "))

def open_port(host, port):
  s = socket.socket()
  try :
    s.connect((host,port))
  except :
    return False

  return True

for port in range(1, num):
  try :
    if open_port(host, port):
      print (f"{GREEN}[+]Port {port} is open ! {RESET}")
    else :
      print("[-]Port ", port , "closed !")
  except :
    print("We got an error :(")
    time.sleep(1)
