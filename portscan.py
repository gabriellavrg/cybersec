import sys
import socket

ip = sys.argv[1]

for p in range(1,65535): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if s.connect_ex((ip, p)) == 0:
        print(f"Porta {p} Aberta!")
        s.close()
