##--------------------------------------
## Pluto Calendar -- Socket Subsystem
## Written by mcsalter
##--------------------------------------
## Todos:
## 1. Complete functionality
## 2. Logging
## 3.

import socket
import threading
import os
import sys

import pluto_classes

AF_INET_HOST = "127.0.0.1"
AF_INET_PORT = 12000
DEFAULT_SOCK_TYPE = socket.AF_INET

AF_UNIX_FILE = "/tmp/PLUTO"


def socket_communicate(sock: socket.SocketType):
    """
    Communication handler for the socket. This reads from and writes to the socket, and as the system requests, pulls data to and from the main program
    @param sock: Socket.Socket
    """
    while True:
        data = sock.recv(1024)
        if not data:
            break
    sock.close()

def socket_handler(port_tuple: tuple = (socket.AF_INET, ("127.0.0.1", 12000))):
    """
    Command to await a socket, and spin up a socket_communicate thread for each new socket connection.
    Currently this only supports AF_INET and AF_UNIX.
    @param port_tuple: tuple of (socket.Address_Family, (connection specs)) -- defaults to localhost port 12000
    @return:
         0 -- operations successful
        -1 -- error found
    """
    with socket.socket(port_tuple[0], socket.SOCK_STREAM) as soc:
        if port_tuple[0] == socket.AF_INET:
            soc.bind((port_tuple[1][0], port_tuple[1][1]))
        elif port_tuple[0] == socket.AF_UNIX:
            soc_name = port_tuple[1]
            if os.path.exists(soc_name):
                os.remove(soc_name)
            soc.bind(soc_name)
        else:
            print(f"WARN: {port_tuple[0]} is currently unsupported, please use an AF_UNIX or AF_INET socket.", file=sys.stderr)
            return
        soc.listen()
        while True:
            conn, addr = soc.accept()
            with conn:
                socket_communicate(conn)
                #socket_thread = threading.Thread(target = socket_communicate, args=conn)
