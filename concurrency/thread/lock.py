# coding:utf8

from threading import (
    Thread,
    currentThread,
    activeCount,
    RLock
)
import time

lock = RLock()

def show(i):
    with lock:
        print currentThread().name, i
        time.sleep(0.1)


def test():
    with lock:
        for i in range(5):
            show(i)


for i in range(2):
    Thread(target=test).start()

