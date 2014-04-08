# coding:utf8

from threading import (
    Thread,
    currentThread,
    activeCount,
)
import time


def test0(s):
    print "ident", currentThread().ident
    print "count", activeCount()
    print s


#Thread(target=test0, args=("Hello",)).start()
#time.sleep(2)

class MyThread(Thread):
    def __init__(self, name, *args):
        super(MyThread, self).__init__(name=name)
        self.data = args

    def run(self):
        print self.name, self.data


#MyThread("abc", range(10)).start()
#time.sleep(2)


def test1():
    print "start..."
    time.sleep(5)
    print "end..."


def run():
    t = Thread(target=test1)
    t.start()
    t.join(2)

    print t.isAlive()
    t.join()

    print "over"

#run()
