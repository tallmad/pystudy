# coding:utf8

def func_singleton(cls):
    def wrap(*args, **kwargs):
        o = getattr(cls, '__instance__', None)
        if not o:
            o = cls(*args, **kwargs)
            cls.__instance__ = o
        return o
    return wrap


def cls_singleton(cls):
    class wrap(cls):
        def __new__(cls, *args, **kwargs):
            o = getattr(cls, '__instance__', None)
            if not o:
                o = cls(*args, **kwargs)
                cls.__instance__ = o
            return o
    return wrap


def action(cls):
    cls.mvc = staticmethod(lambda: "Action")
    return cls
