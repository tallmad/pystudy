# coding:utf8

from multiprocessing import Process
from os import getpid
from signal import signal, SIGTERM
from time import sleep


def test():
    def handler(signum, frame):
        print "child exit.", getpid()
        exit(0)

    signal(SIGTERM, handler)
    print "child start:", getpid()
    while True: sleep(1)


if __name__ == "__main__":
    p = Process(target=test)
    p.daemon = True
    p.start()

    sleep(2)
    print 'parent exit.'
