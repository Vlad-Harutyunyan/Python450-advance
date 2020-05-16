import socket
import json
import random
IP = '178.0.0.1'
PORT = 8028
SIZE = 1024 # in bytes



board = {
    1:[' ',' ',' '],
    2:[' ',' ',' '],
    3:[' ',' ',' '],
}


def CheckVictory(board, t):

    if board[1][0]  == t and  board[1][1] == t and board[1][2] == t :
        return True
    elif board[2][0]  == t and  board[2][1] == t and board[2][2] == t :
        return True
    elif board[3][0]  == t and  board[3][1] == t and board[3][2] == t :
        return True
    elif board[1][0]  == t and  board[2][1] == t and board[3][2] == t :
        return True 
    elif board[1][0]  == t and  board[2][0] == t and board[3][0] == t :
        return True
    elif board[1][1]  == t and  board[2][1] == t and board[3][1] == t :
        return True
    elif board[1][2]  == t and  board[2][2] == t and board[3][2] == t :
        return True
    elif board[3][2]  == t and  board[2][1] == t and board[3][0] == t :
        return True
    return False


def checkOver(board) :
    for x in board:
        if ' ' in board[x]:
            return False
    return True


with  socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock: 
    sock.bind(('',PORT))
    sock.listen(4)
    conn , addr = sock.accept()
    print('Connected by ' , addr)
    
    with conn:
        while True :
            r = None
            data = (conn.recv(SIZE).decode()).split(',')
            print(data)
            if int(data[0]) > 3 :
                r = json.dumps('[error] row index out of range !')
            elif int(data[1]) >= 3 :
                r = json.dumps('[error] col index out of range !')
            elif board[int(data[0])] [int(data[1])] == 'X' or board[int(data[0])] [int(data[1])] == 'O' :
                r = json.dumps('[error] this cell is busy')
            elif CheckVictory(board,'O'):
                r = json.dumps('[lose] O won !')
            elif checkOver(board) :
                r =  json.dumps('[draw] game end!')
            else :
                board[int(data[0])] [int(data[1])] = 'X'
                if CheckVictory(board,'X'):
                    r = json.dumps('[win] X won !')
                else :  
                    for x in range (20):
                        rand_x = random.randint(1,3)
                        rand_y = random.randint(0,2)
                        if board[rand_x][rand_y] != 'X' and board[rand_x][rand_y] != 'O':
                            board[rand_x][rand_y] = 'O'
                            break
                    r = json.dumps(board)
                    


            conn.sendall(r.encode())

            
