from matplotlib import pyplot as plt

a = 10
c = float(8/3)

def x_dash(xn, yn):
    xn1 = a * (yn - xn)
    return xn1

def y_dash(xn, yn, zn, b):
    yn1 = -(xn * zn) + (b * xn) - yn
    return yn1

def z_dash(xn, yn, zn):
    zn1 = (xn * yn) - (c * zn)
    return zn1

x0 = 1.0
y0 = 0.0
z0 = 0.0
h = 0.01
t = 0.0


def func_calc(b, x0, y0, z0, t):
    T = []
    X = []
    Y = []
    Z = []
    while t <= 50:
        k1 = h * x_dash(x0, y0)
        k2 = h * x_dash(x0 + ((k1)/2), y0)
        k3 = h * x_dash(x0 + ((k2)/2), y0)
        k4 = h * x_dash(x0 + k3, y0)
        kx = (k1 + 2 * k2 + 2 * k3 + k4)/6
        # print(k1, k2, k3, k4)
        xn1 = x0 + kx

        k1 = h * y_dash(x0, y0, z0, b)
        k2 = h * y_dash(x0, y0 + ((k1)/2), z0, b)
        k3 = h * y_dash(x0, y0 + ((k2)/2), z0, b)
        k4 = h * y_dash(x0, y0 + k3, z0, b)
        ky = (k1 + 2 * k2 + 2 * k3 + k4)/6
        yn1 = y0 + ky

        k1 = h * z_dash(x0, y0, z0)
        k2 = h * z_dash(x0, y0, z0 + ((k1)/2))
        k3 = h * z_dash(x0, y0, z0 + ((k2)/2))
        k4 = h * z_dash(x0, y0, z0 + k3)
        kz = (k1 + 2 * k2 + 2 * k3 + k4)/6
        zn1 = z0 + kz

        t = t + h
        x0 = xn1
        y0 = yn1
        z0 = zn1
        # print(zn1)
        X.append(xn1)
        Y.append(yn1)
        Z.append(zn1)
        T.append(t)
        
    return X, Y, Z, T

X5, Y5, Z5, T5 = func_calc(5, 1.0, 0.0, 0.0, 0.0)
X10, Y10, Z10, T10 = func_calc(10, 1.0, 0.0, 0.0, 0.0)
X25, Y25, Z25, T25 = func_calc(25, 1.0, 0.0, 0.0, 0.0)

plt.plot(T5, Z5, color='r', label='b = 5')
plt.plot(T10, Z10, color='g', label='b = 10')
plt.plot(T25, Z25, color='b', label='b = 25')

plt.xlabel("Time")
plt.ylabel("Z")
plt.legend()

plt.show()