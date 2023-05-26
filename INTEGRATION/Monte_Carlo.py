from cmath import pi
from random import random
import matplotlib.pyplot as plt

def funct(x):
    s = float(1/(1+ x**2))
    return s

N = int(input("Enter no. of points:"))
a = float(input("Enter lower limit:"))
b = float(input("Enter upper limit:"))
h = (b - a) / N
s = 0.0
splt = []
splt1 = []

for i in range(0, N):
    splt.append(funct(random()))
    s += splt[i]
    splt1.append(s*(b-a)/(i+1))

s *= h
print("Integral calculated using Monte Carlo method is", s)
ex = pi / 4
print("Expected Integral value is", ex)
er = (abs(ex - s) / ex) * 100
print("Error is", er, "%")
plt.plot(splt1)
plt.show()