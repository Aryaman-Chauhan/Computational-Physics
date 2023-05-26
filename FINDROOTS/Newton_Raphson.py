import matplotlib.pyplot as plt

def func(x):
    fx = x**3 - 0.165*x*x +3.993*(10**-4)
    fdx = 3*x*x - 0.330 * x
    return fx, fdx
guess = float(input("Enter Your Guess:"))
iterr = int(input("Enter no. of iterations:"))
tol = float(input("Enter Tolerance:"))
xi = []
fxg = []
xi.append(guess)
print(xi[0])
t = 0
for i in range(0, iterr):
    fx, fdx = func(xi[i])
    fxg.append(fx)
    rat = fx / fdx
    xi1 = xi[i] - rat
    print(i+1,":i+1th x is", xi1,", when xi is", xi[i])
    err = abs(xi1 - xi[i])/xi[i] * 100
    xi.append(xi1)
    if err <= tol:break
    t = i
print("Root calculated is:", xi[t])
fx,_ = func(xi[t])
fxg.append(fx)
print("f(x) at x =", xi[t],"is", fx)
plt.plot(fxg,xi)
plt.show()