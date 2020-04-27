import socket
from configparser import ConfigParser
import os
import datetime

#dirname
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'config.ini')
config = ConfigParser()
config.read(initfile)


IP = config.get('socket','ip')
PORT = config.getint('socket','port')

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('',PORT))
d = datetime.datetime.now()

print('Welcome :) , print help for commands !')

while True:
    user_input = input('command : ')
    client.sendall(user_input.encode())
    data = client.recv(1024)
    
    if user_input == 'exit':
        break
    elif user_input == 'help':
        print('commands ` \n 1) day - return current day \n 2) month - return current month \n 3) time - return  current time format hour:minute  \n 4) year - return current year \n 5) exit - close program')
    elif user_input == 'day':
        print(d.day)
    elif user_input == 'month':
        print(d.month)
    elif user_input == 'time':
        print(f'{d.hour}:{d.minute}')
    elif user_input == 'year':
        print(d.year)
    else :
        print(f'Unrecognized command \'{user_input}\' :(')
client.shutdown(socket.SHUT_RDWR)
client.close()