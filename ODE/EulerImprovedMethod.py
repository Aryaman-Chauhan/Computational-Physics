# Called Runge Kutta Method of Second Order

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
    ys = yd + h * func(xd, yd)
    yd = yd + (func(xd, yd) + func(xd + h, ys)) * h/2
    xd += h
    s -= 1

print("Value of y is:", yd)