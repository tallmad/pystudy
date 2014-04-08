# coding:utf8

"""
semaphore 通过计数器来限制线程运行数量
acquire()递减计数器，release()增加计数器
"""

from threading import Thread, Semaphore, currentThread
from time import sleep

sem = Semaphore(2)


def test():
    with sem:
        for i in range(5):
            print currentThread().name, i
            sleep(0.1)


for i in range(5):
    Thread(target=test).start()
