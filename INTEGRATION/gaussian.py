from cmath import pi

def funct(x):
    x = float(1/(1+ x**2))
    return x

def scaler(a, b, t):
    t = (b + a) / 2 + (b - a) * t / 2
    return t

t = list()
w = list()
print("When entering the points, ensure that you enter them in ascending order.")
i = 0
while(1):
    a = input("Enter point, or q to end this iteration:")
    if a == 'q': break
    t.append(float(a))
    w.append(float(input("Enter corresponding weight:")))
    i += 1

a = float(input("Enter lower limit:"))
b = float(input("Enter upper limit:"))
h = (b - a) / 2

for i in range(0, len(t)):
    t[i] = funct(scaler(a, b, t[i]))

s = 0.0
for i in range(0, len(t)):
    s += t[i]*w[i]

s *= h
print("Integral calculated using Gaussian method is", s)
ex = pi / 4
print("Expected Integral value is", ex)
er = (abs(ex - s) / ex) * 100
print("Error is", er, "%")