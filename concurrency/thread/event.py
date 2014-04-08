# coding:utf8

from threading import Event, Thread
from time import sleep

"""
e.wait() block thread until internal flag is set to True
e.set() will set flag=True
e.clear() set internal flag=False which will make wait() block thread
e.isSet() to check flag value

every thread should have an independent Event
"""

def test():
    e = Event()
    def test():
        for i in range(5):
            e.wait()

            e.clear()
            print i
    Thread(target=test).start()
    return e

e = test()

for i in range(5):
    sleep(2)
    print e.isSet()
    e.set()
    print e.isSet()

