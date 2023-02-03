import socket
from pymemcache.client.base import Client

def client_program():
    client = Client('localhost:5000')
    # client.set('some_key', 'some_value', 3)
    # client.set('some_key', 'some_value', 10)
    client.set('some_key', 'some_value')
    result = client.get('some_key')

if __name__ == '__main__':
    client_program()