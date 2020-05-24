import os
import sys
import time
#lib to install : argparse


#printing logo
logo = ("""\

  ___           _   _    _  _     _
 |   \ ___ __ _| |_| |_ | \| |___| |_ ___
 | |) / -_) _` |  _| ' \| .` / _ \  _/ -_)
 |___/\___\__,_|\__|_||_|_|\_\___/\__\___|

""")

print("--[made by PS]--")
# getting input

def main () :
  try:
    print(logo)
    print("Welcome!")
    print("Printing options...")
    time.sleep(1)
    print ("1)start ddos tool")
    print ("2)start port scanner")
    print ("3)start vulnerability quick test")
    print ("4)start xss test")
    print ("5)start sqli test")
    print ("6)help")
    print ("99)quit")
    cho = int(input("What shall it be : "))
    if cho == 1:
      try :
        print("getting ddos tool ready")
        os.system("python3 ddos.py")
      except :
        print("the ddos tool does not work or does not exists !")
    elif cho == 2 :
      print("Starting port scanner")
      print("1)quick scan")
      print("2)intense scan")
      p_scan = int(input("-> "))
      if p_scan == 1 :

        os.system("python3 speed_scan.py")
      elif p_scan == 2 :
        os.system("python3 acc_scan.py")
      else:
        print('nope')
        sys.exit()
    elif cho == 6 :
      print("In order to use a module you need to specify the number of it")
    elif cho == 99 :
      print("Bye !")
      time.sleep(1)
      sys.exit()
    else :
      print("Sorry , the module does not exists or is still in DEV :)")
      main()
  except :
    print("Sorry , we have a problem here :) , bye !")

if __name__ == '__main__':
  main()




