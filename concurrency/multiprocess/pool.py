# coding:utf8

from time import sleep
from multiprocessing import Pool

def test0(*args, **kwargs):
    print args
    print kwargs
    return 123

def run_apply():
    pool = Pool()
    print pool.apply(test0, range(3), dict(a=1, b=2))
    pool.close()
    pool.join()


def test1():
    sleep(2)
    return 123


def callback(ret):
    sleep(2)
    print "return:", ret



def run_apply_async():

    pool = Pool()
    pool.apply_async(test1, callback=callback)

    ar = pool.apply_async(test1)
    print ar.get()

    pool.close()
    pool.join()


if __name__ == "__main__":
    run_apply_async()
