import socket

def client_program():
    host = "127.0.0.1"  # as both code is running on same pc
    port = 5001  # socket server port number

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'exit':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()