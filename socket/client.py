if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    import time
    #time.sleep(2)
    sock.send('1')
    sock.close()
    time.sleep(12)
    print sock.recv(1024)
