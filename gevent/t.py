'''
refer to http://stackoverflow.com/questions/22442100/gevent-monkey-patch-all-breaks-code-that-relies-on-socket-shutdown # noqa
'''
from gevent import monkey

monkey.patch_all()

import os
import select
import socket
import threading
import time


class SocketReadThread(threading.Thread):
    def __init__(self, socket):
        super(SocketReadThread, self).__init__()
        self._socket = socket
        self._socket.setblocking(0)
        r, w = os.pipe()
        self._cancelpipe_r = os.fdopen(r, 'r')
        self._cancelpipe_w = os.fdopen(w, 'w')

    def run(self):
        connected = True
        read_fds = [self._socket, self._cancelpipe_r]
        while connected:
            print "Calling select"
            read_list, write_list, x_list = select.select(read_fds, [], [])
            print "Select returned"
            if self._cancelpipe_r in read_list:
                print "exiting"
                self._cleanup()
                connected = False
            elif self._socket in read_list:
                print "calling socket.recv"
                data = self._socket.recv(1024)
                if (len(data) < 1):
                    print "received nothing, assuming socket shutdown"
                    connected = False
                    self._cleanup()
                else:
                    print "Recieved something: {}".format(data)

    def stop_reading(self):
        print "writing to pipe"
        self._cancelpipe_w.write("\n")
        self._cancelpipe_w.flush()
        print "joining"
        self.join()
        print "joined"

    def _cleanup(self):
        self._cancelpipe_r.close()
        self._cancelpipe_w.close()
        self._socket.shutdown(socket.SHUT_RDWR)
        self._socket.close()


if __name__ == '__main__':

    sock = socket.socket()
    sock.connect(('127.0.0.1', 4242))

    st = SocketReadThread(sock)
    st.start()
    time.sleep(3)
    st.stop_reading()
