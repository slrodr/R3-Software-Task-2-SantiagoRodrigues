import socket
import msvcrt

#Socket setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1435))


while True:
    key = msvcrt.getch()   #Collect the key input
    s.send(key)

    data = s.recv(1024)
    print (f"Sent key: {data}")  #prints the data sent to the server for checking

s.close()
