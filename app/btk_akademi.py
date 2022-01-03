import math
import time

def calculate_time(func):
    def inner(*arg,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*arg,**kwargs)
        finish = time.time()  
        print("Bu işlem" +" "+ str(finish-start)+" "+ "saniye sürdü.") 
    return inner
    
@calculate_time
def toplama(a,b):
    return a+b
@calculate_time
def carpma(a,b):
    return a*b
@calculate_time
def liste(a):
    return list(a)
@calculate_time
def tuples(a):
    return tuple(a)
toplama(2,3)
carpma(2,3)
liste([1,2,3])
tuples((1,2,3))
