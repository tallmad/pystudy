if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8001))
    sock.listen(5)
    while True:
        connection,address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            import time
            print time.time()
            time.sleep(5)
            if buf == '1':
                connection.send('welcome to server!')
            else:
                connection.send('please go out!')
            print time.time()
            connection.send('welcome to server! again')
        except socket.timeout:
            print 'time out'
        connection.close()
