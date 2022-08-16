import socket
import time
from threading import Timer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.blind(('', 5000))
s.listen(5)
print("Server is now running")

def background_controler():
    message = "Hellow client"
    print(message)
    clientsocket.send(bytes(message, "utf-8"))
    Timer(5, background_controler).start()
background_controler()

while True:
    clientsocket, adress = s.accept()
    print(f"Connection from {adress} has been established")
    background_controler()
