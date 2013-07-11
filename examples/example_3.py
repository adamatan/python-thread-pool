#!/usr/bin/python

import time
import datetime
from multiprocessing.pool import ThreadPool

def square(num):
    """Returns the square of num."""
    time.sleep(2)
    return num**2

pool = ThreadPool(processes=4)               # Thread pool with at most 4 concurrent threads
results = pool.map_async(square, range(10))  # Add 10 threads to the pool, asynchronously

print("Started the thread pool.")

while not results.ready():                   # Do something while waiting  
    time.sleep(1)
    print("%-15s Main thread is doing something in the meanwhile" % (datetime.datetime.now()))
    
print("Thread pool done finished, successfull?=%s" % results.successful())
print("Results: %s"%results.get())