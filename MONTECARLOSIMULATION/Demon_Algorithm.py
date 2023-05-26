import random
import matplotlib.pyplot as plt
import math

N = int(input("Enter no. of Particles: "))
E = float(input("Enter total Energy of System: "))
E_d = 0.
dv_max = float(input("Enter max. velocity change allowed: "))
mcs = int(input("Enter no. of Monte Carlo Simulation: "))
v_list = []
v_plot_list = []
E_plot_list = []
v_initial = math.sqrt(2 * E)/N
for i in range(N):
    v_list.append(v_initial)

count = 0
E_sum = 0.
E_d_sum = 0.

for i in range(0, mcs):
    for j in range(0, N):
        rnd = random.random()
        dv = float(2 * rnd - 1) * dv_max
        # print(v)
        ipart = int(rnd*(N-1)) # Selecting a random particle
        vtrial = v_list[ipart] + dv
        E_change = (float(vtrial**2) - float(v_list[ipart]**2)) / 2

        if(E_change < E_d):
            v_list[ipart] = vtrial
            E_d = E_d - E_change
            E = E + E_change
            count += 1
    E_sum += E
    E_d_sum += E_d
    vsum = 0.
    Esum = 0.
    for i in range(N):
        vsum += v_list[i]
        Esum += (v_list[i]**2)/2
    v_plot_list.append(vsum)
    E_plot_list.append(Esum*N)

E_sum_avg = E_sum / (mcs * (count+1))
E_d_sum_avg = E_d_sum / mcs

print(E_d, E, count)
print(E_sum_avg, E_d_sum_avg)

plt.subplot(2,1,1)
plt.plot(range(mcs), v_plot_list)
plt.subplot(2,1,2)
plt.plot(range(mcs), E_plot_list)
plt.show()
