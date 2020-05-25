from socket import *
import time, sys
from datetime import datetime

host = ' '
common_ports = [
    20,
    21,
    22,
    23,
    24,
    25,
    53,
    80,
    110,
    120,
    123,
    125,
    135,
    143,
    161,
    194,
    443
    ]



try :
  host = input("[+]Target ->")
  print("[*]Target ", host)
except KeyboardInterrupt :
  print("[!]Well, bye !")
  time.sleep(1)
  sys.exit()

hip = gethostbyname(host)

print("""
    You have 3 options :
    1)Start a normal scan
    2)Badass intense scan
    3)Quick scan
    Any other number will consider a quit option

""")

cho = int(input("-> "))
def normal():
  print("lol")
if cho == 1 :
  print("[+]Starting normal scan")
  time.sleep(1)
  normal()

elif cho == 2 :
  print("[+]Starting intense scan")
  time.sleep(1)
  intense()
elif cho == 3 :
  print("[+]Starting quick scan")
  time.sleep(1)
  quick()

else :
  print("See ya !")
  sys.exit(1)

def scan_port(host, port , r_port=1):
  try :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect_ex(host, port)
    if conn == 0 :
      r_code == conn
    s.close()
  except Exception as e :
    pass
  return r_code


def normal(host):
  for port in range(1, 1000):
    try:
      response = scan_port(host, port)
      if response == 0 :
        print("[!] Port %d : Open" % (port))
    except Exception as e :
      pass
def quick():
  print("Still in dev")

def intense():
  print("Still in dev")


