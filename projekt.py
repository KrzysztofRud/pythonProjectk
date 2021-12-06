import matplotlib.pyplot as plt
import numpy
import numpy as np
import pylab
import math

def dodawanie(q, p):
    return q+p;
def dlugosc_w(o):
    return math.sqrt(o[0]*o[0]+o[1]*o[1]);
def przyspiesenie(d,b):
    return d/b;
g = 6.6743015*10**(-11)*5.9736*10**24/(6373140**2)
a = int(input())
b = int(input())
B = numpy.array([a, b])
c = int(input())
d = int(input())
C = numpy.array([c, d])
print(B)
print(C)
print(dodawanie(B, C))
print(dlugosc_w(B))
print(g)