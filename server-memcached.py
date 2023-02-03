# import socket programming library
import socket
import random
import time

# import thread module
from _thread import *
import threading

#TODO test dictionary
dataDict = {
    "key1": {
        "bytes": 4,
        "value": "val1"
    },
    "key2": {
        "bytes": 4,
        "value": "val2"
    },
    "key3": {
        "bytes": 4,
        "value": "val3"
    }
}

print_lock = threading.Lock()

# thread function
def threaded(conn):
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        message = data.split("\r\n")
        print("message: ", message)
        break
        if message[0] == 'set':
            # Get/set operations can be very fast.Adding small random delay for all of them on the server.
            data = data.replace("\n", " ").replace("\r", " ")
            print("data:",data)
            message = data.split()
            print ("message:",message)
            print("data:\n",message[1],message[3],message[-1])
            time.sleep(random.uniform(0, 1))
            data = setData(message[1],message[3],message[-1])
        elif message[0] == 'get':
            time.sleep(random.uniform(0, 1))
            data = getData(message[1])
        else:
            data = "please write a valid func: set or get"

        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

# get function
def getData(getKey):
    print_lock.acquire()
    message = ""
    if getKey in dataDict.keys():
        message += "VALUE " + getKey + " " + str(dataDict[getKey]["bytes"]) + "\n" + dataDict[getKey]["value"] + "\n\r" + "END\n\r"
        print(message)
    else:
        message += "NOT_FOUND\r\n"
        print(message)
    print_lock.release()
    return message

# set function
def setData(setKey,setByte,setValue):
    print_lock.acquire()
    print("setData function was called", setKey,setByte, len(setValue))
    # check if the len of the setByte and the sevValue are ==
    if int(setByte) == len(setValue):
        dataDict.update({setKey: {"bytes":setByte,"value":setValue}})
        print_lock.release()
        print("\nSTORED")
        return "\nSTORED"
    else:
        print_lock.release()
        print("\nNOT-STORED")
        return "\nNOT-STORED"

def Main():
    ThreadCount = 0
	# get the hostname
    host = ""
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    print("socket binded to port", port)
	# configure how many client the server can listen simultaneously
    server_socket.listen(5)
    print("socket is listening")

	# a forever loop until client wants to exit
    while True:
		# establish connection with client
        conn, address = server_socket.accept()  # accept new connection
        print('Connected to :', address[0], ':', address[1])

		# Start a new thread and return its identifier
        start_new_thread(threaded, (conn,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    server_socket.close()


if __name__ == '__main__':
	Main()

