import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5003))

while True :
    user_says = input('Say something : ')
    client.sendall(user_says.encode())
    data = client.recv(1024)


    print(data)

client.shutdown(socket.SHUT_RDWR)
client.close()