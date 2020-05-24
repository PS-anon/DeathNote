import socket
from colorama import init, Fore
init()
RESET = Fore.RESET
GREEN = Fore.GREEN
host = input("[+]Target  ip : ")
num = int(input("How many ports do you want to test for : "))

def open_port(host, port):
  s = socket.socket()
  try :
    s.settimeout(0.2)
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
    print("error, bye !")
