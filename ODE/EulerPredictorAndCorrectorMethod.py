# Also called Euler Modified Method 

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
    xm = xd + h/2
    ym = yd + func(xd, yd) * h/2
    yd = yd + h * func(xm, ym)
    xd+=h
    s -= 1

print("Value of y is:", yd)