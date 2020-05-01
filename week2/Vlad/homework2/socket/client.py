import socket
from configparser import ConfigParser
import os

#dirname
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'config.ini')
config = ConfigParser()
config.read(initfile)


IP = config.get('socket','ip')
PORT = config.getint('socket','port')

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((IP,PORT))

print('Welcome :) , print help for commands !')

while True:
    user_input = input('command : ')
    
    if user_input == 'exit':
        client.sendall(user_input.encode())
        break
    elif not len(user_input):
        print('empty')
    else :
        client.sendall(user_input.encode())
        data = client.recv(1024)
        print(data.decode("utf-8")) 

client.shutdown(socket.SHUT_RDWR)
client.close()