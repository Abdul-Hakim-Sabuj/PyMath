import time
import sys
import math

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def cau_sub(a,b):
    if(a>b):
        return a-b
    elif(b>a):
        return b-a
    else:
        return 0
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def cau_div(a,b):
    if(a>b):
        return a/b
    elif(b>a):
        return b/a
    else:
        return 1
def mod(a,b):
    return a%b
def sqr(a):
    return a*a
def pow(a,b):
    return a**b
def pi():
    return math.pi()
def PyGorus():
    return "A^2+B^2=C^2"
def id_PyGorus(a,b):
    c=((a**2)+(b**2))
    return c**2
def id_PyGorus_2(a,b):
    c=((a**2)+(b**2))
    return c
def byte(a):
    d= bytes(a)
    a=str(d)
    a=a.replace('b','')
    a=a.replace('\'\'','')
    return a
def bina(a):
    d= bin(a)
    a=str(d)
    a=a.replace('0b','')
    a=a.replace('\'\'','')
    return int(a)
def octa(a):
    d= oct(a)
    a=str(d)
    a=a.replace('0o','')
    a=a.replace('\'\'','')
    return a
def hexa(a):
    d= hex(a)
    a=str(d)
    a=a.replace('0h','')
    a=a.replace('\'\'','')
    return a
def sqrt(a):
    return math.sqrt(a)
def delay(a):
    return time.sleep(a)
def compute(a):
    return sys.stdout.write(f'{a}')