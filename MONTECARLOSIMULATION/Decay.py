import matplotlib.pyplot as plt
import numpy as np

# Set the initial number of particles, decay probability, and time range
N = int(input("Enter no. of particles: "))
p = float(input("Enter decay Probability: "))
t = int(input("Enter time range:"))
population = []

for i in range(t):
    Nn = np.random.rand(N)
    survive = np.sum(Nn > p)    
    population.append(survive)
    N = survive

# Plot the number of particles as a function of time
plt.plot(range(t), population)
plt.xlabel('Time')
plt.ylabel('Number of particles')
plt.show()
