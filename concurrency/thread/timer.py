# coding:utf8

"""
timer 独立线程在n秒后执行某个函数
若timer尚未执行， 可用cancel取消
"""

import datetime
from threading import Timer

def test():
    print datetime.datetime.now()

test()
t = Timer(2, test)
t.start()
#t.cancel()
