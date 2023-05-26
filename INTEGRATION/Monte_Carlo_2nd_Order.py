from random import random

def funct(x, y):
    s = float(x * x + 6 * x * y + y * y)
    return s

N = int(input("Enter no. of points:"))
a = float(input("Enter lower limit of x:"))
b = float(input("Enter upper limit of x:"))
c = float(input("Enter lower limit of y:"))
d = float(input("Enter upper limit of y:"))

s = 0.0
hx = (b - a) / N
hy = (d - c) / N
sx = a
sy = c

# while sx < b:
#     sx += hx
#     while sy < d:
#         s += funct(random() , random())
#         sy += hy

for i in range(N):
    s += funct(random() , random())

s = s * hx 
print("Integral calculated using Monte Carlo method is", s)
ex =  2/3 #+ 1.5
print("Expected answer:", ex)
er = (abs(ex - s) / ex) * 100
print("Error:", er)