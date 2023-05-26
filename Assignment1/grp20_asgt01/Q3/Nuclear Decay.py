import numpy as np
import matplotlib.pyplot as plt

p=0.01  #probability of decay
q=1-p
N=500   # number of particles
time = 1000

def decay(N):
    population=[]
    for _ in range(N):
        r=np.random.random(N)      
        survive=np.sum(r<q) 
        population.append((survive))
        N=survive
    return population
x=range(N)
plt.plot((x), decay(N), color = 'g') 
plt.show()  