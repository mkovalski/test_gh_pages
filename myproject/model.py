#!/usr/bin/env python

class ModelBase(object):
    ''' The base class

    Args:
        x (int): var 1
        y (int): var 2

    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y


class InheritedModel(ModelBase):
    def __init__(self, *args, **kwargs):
        ModelBase.__init__(self, *args, **kwargs)


if __name__ == '__main__':
    model = InheritedModel(x = 1, y = 2)
