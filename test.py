import numpy as np

# Set the value of lambda
lam = 1.0

# Generate a sequence of random numbers using x = lambda * ln(r)
r = np.random.random(10000)
x = lam * np.log(r)
x = np.abs(x)

# Plot the histogram of the sequence x
import matplotlib.pyplot as plt
plt.hist(x, bins=50, density=True)

# Overlay the expected exponential distribution
x_values = np.linspace(0, 5, 100)
y_values = 1/lam * np.exp(-x_values/lam)
plt.plot(x_values, y_values, 'r')

plt.show()
