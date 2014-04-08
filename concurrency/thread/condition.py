# coding:utf8

"""
condition is like a combination of event and lock
wait() 临时让出锁，阻塞当前线程, 直到notify()发送通知再次请求锁来恢复执行
notifyAll() 激活所有线程，会让所有获取锁的线程自己去抢锁
"""

from threading import Thread, currentThread, Condition
from time import sleep


cond = Condition()


def t1():
    with cond:
        for i in range(5):
            print currentThread().name, i
            sleep(0.1)
            if i == 2: cond.wait()


def t2():
    with cond:
        for i in range(5):
            print currentThread().name, i
            sleep(0.1)
        cond.notify()


Thread(target=t1).start()
Thread(target=t2).start()


sleep(2)
print '=======\n'

Thread(target=t1).start()
Thread(target=t1).start()

sleep(2)
print '=======\n'

with cond:
    cond.notifyAll()
