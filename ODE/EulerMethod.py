# Called Runge Kutta Method of First Order

def func(xn, yn):
    return 2 * xn * yn

s = int(input("Step size:"))
a = float(input("Lower limit of x:"))
b = float(input("Upper limit of x:"))
y0 = float(input("y0 value at lower limit of x:"))

xd = a
h = float((b - a)/s)
yd = y0 + h * func(a, y0)

while(s >= 1):
    xd += h
    yd = yd + h * func(xd, yd)
    s -= 1

print("Value of y is:", yd)