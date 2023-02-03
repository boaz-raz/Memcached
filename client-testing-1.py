import socket

def client_program():
    host = "127.0.0.1"  # as both code is running on same pc
    port = 5001  # socket server port number

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))  # connect to the server

    messages = ["get", "set key4 4 val4", "get", "set key5 5 val5", "get"]

    for message in messages:
        print("sending message to server: " +  message + "\n")
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()