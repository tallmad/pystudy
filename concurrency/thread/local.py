# coding:utf8

"""
local 为线程提供独立的存储空间
"""

from time import sleep
from threading import Thread, local, currentThread

data = local()


def test(fn, x):
    data.x = x
    for i in range(5):
        data.x = fn(data.x)
        print currentThread().name, data.x
        sleep(0.2)


t1 = (lambda x: x + 1, 0)
t2 = (lambda x: x + 'a', 'a')

Thread(target=test, args=t1).start()
Thread(target=test, args=t2).start()
