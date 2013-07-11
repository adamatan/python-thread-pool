#!/usr/bin/python

import time
import datetime
from multiprocessing.pool import ThreadPool

def square(num):
    """Returns the square of num."""
    print("%-15s Calculating the square of %d" % (datetime.datetime.now(), num))
    time.sleep(2)
    return num**2

pool = ThreadPool(processes=4)     # Thread pool with at most 4 concurrent threads
print pool.map(square, range(10))  # Add 10 threads to the pool, run blocking
print "Done"