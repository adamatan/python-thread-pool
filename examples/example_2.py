#!/usr/bin/python

import time
import datetime
from multiprocessing.pool import ThreadPool

class Square(object):
    def __init__(self, num):
        self.num = num
        time.sleep(2)
        
    def get_result(self):
        return "The square of %d is %d" % (self.num, self.num**2)

pool    = ThreadPool(processes=4)      
squares = pool.map(Square, range(10))  # Square calls Square.__init__
print squares                          # A list of objects
print [square.get_result() for square in squares] # A list of Strings