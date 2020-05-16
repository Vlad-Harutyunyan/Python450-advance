import socket
import json

IP = '127.0.0.1'
PORT = 8028
SIZE = 1024 # in bytes
  
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((IP,PORT))


def printBoard(brd):
    print(brd['1'][0] + '|' +brd['1'][1] + '|' + brd['1'][2])
    print('-+-+-')
    print(brd['2'][0] + '|' +brd['2'][1] + '|' + brd['2'][2])
    print('-+-+-')
    print(brd['3'][0] + '|' +brd['3'][1] + '|' + brd['3'][2])





while True:
    user_input = input('Possition : ')
    
    if user_input == 'exit':
        client.sendall(user_input.encode())
        break
    elif not len(user_input):
        print('empty')
    else :
        client.sendall(user_input.encode())
        data =  json.loads(client.recv(SIZE).decode("utf-8"))
        if '[error]' in data:
            print(data)
        elif '[win]' in data :
            print('You won')
        elif '[lose]' in data :
            print('You lose')
        elif '[draw]' in data :
            print('game end with draw !!!')
        else:
            printBoard(data)


client.shutdown(socket.SHUT_RDWR)
client.close()