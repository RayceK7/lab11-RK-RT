# https://github.com/RayceK7/lab11-RK-RT
#Partner 1: Rayce Kronenberg
#Partner 2: Ragul Thiyagarajan
# First example
import math

def sqrt(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)
def hypotenuse(a,b):
    return math.hypot(a,b)
def add(a, b): 
    return a + b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a * b
def divide(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return a / b
def log(a,b):
    if b >= 1:
        raise ValueError
    else:
        return log(a,b)
def exp(a,b):
    return a ** b



