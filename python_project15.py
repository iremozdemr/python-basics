import time
import math

def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("time: ",end-begin)
    return inner

@calculate_time
def factorial(num):
    time.sleep(2)
    result = math.factorial(num)
    print(result)

factorial(10)