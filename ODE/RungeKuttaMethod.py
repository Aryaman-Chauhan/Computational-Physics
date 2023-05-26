# Runge-Kutta Method of the 4th Order

def func(xn, yn):
    return 2 * xn * yn

s = int(input("Step size:"))
a = float(input("Lower limit of x:"))
b = float(input("Upper limit of x:"))
y0 = float(input("y0 value at lower limit of x:"))

xd = a
h = float((b - a)/s)
yd = y0

while(s >= 1):
    k1 = h * func(xd, yd)
    k2 = h * func(xd + h/2, yd + k1/2)
    k3 = h * func(xd + h/2, yd + k2/2)
    k4 = h * func(xd + h, yd + k3)
    k = (k1 + 2 * k2 + 2 * k3 + k4)/6
    yd = yd + k
    s -= 1
    xd += h

print("Value of y is:", yd)