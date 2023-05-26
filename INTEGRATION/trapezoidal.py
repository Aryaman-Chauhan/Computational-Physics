from cmath import pi

def funct(x):
    s = float(1/(1+ x**2))
    return s

N = float(input("Enter no. of points:"))
a = float(input("Enter lower limit:"))
b = float(input("Enter upper limit:"))
h = (b - a) / N
s = float(funct(a) / 2)
s += funct(b) / 2
k = a + h

while k < b:
    s += funct(k)
    k += h
s *= h

print("Integral calculated using Trapezoidal method is", s)
ex = pi / 4
print("Expected Integral value is", ex)
er = (abs(ex - s) / ex) * 100
print("Error is", er, "%")