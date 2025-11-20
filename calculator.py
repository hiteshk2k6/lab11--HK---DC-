#https://github.com/hiteshk2k6/lab11--HK---DC-.git
#Hitesh K
#Nobody
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm arguments must be positive")
    if a == 1:
        raise ValueError("Logarithm base cannot be 1")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    if a < 0 or b < 0:
        raise ValueError("Cannot have negative side lengths")
    return math.hypot(a, b)

