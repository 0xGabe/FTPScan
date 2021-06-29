import sys
import socket

def prPink(skk): print("\033[95m{}\033[00m" .format(skk))
def prRed(skk): print("\033[91m{}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk))

prPink("""                                                         
     dBBBBP dBBBBBBP dBBBBBb        
                         dB'        
   dBBBP     dBP     dBBBP'         
  dBP       dBP     dBP             
 dBP       dBP     dBP              
                                    
  .dBBBBP   dBBBP dBBBBBb     dBBBBb
  BP                   BB        dBP
  `BBBBb  dBP      dBP BB   dBP dBP 
     dBP dBP      dBP  BB  dBP dBP  
dBBBBP' dBBBBP   dBBBBBBB dBP dBP               
""")

if len(sys.argv) != 3:
    prRed("[-] How to use -> python 10.0.0.10 22")
else:
    ip = sys.argv[1]
    port = sys.argv[2]

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((ip,int(port)))
    banner = mysocket.recv(1024)

    prPurple("[i] Server Banner")
    print(banner)

    prGreen("[+] Test Default User and Password")
    mysocket.send("USER anonymous\r\n")
    user = mysocket.recv(1024)
    print(user)
    
    prGreen("[+] Login Successful")
    mysocket.send("PASS anonymous\r\n")
    password = mysocket.recv(1024)
    print(password)

    
    prGreen("[+] Current Directory")
    mysocket.send("PWD \r\n")
    info = mysocket.recv(2048)
    print(info)

    
