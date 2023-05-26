import numpy as np
import matplotlib.pyplot as plt

def calc_acceleration(positions, sigma, epsilon):
    num_molecules = positions.shape[0]

    # Initialize an array to store the accelerations
    accelerations = np.zeros((num_molecules, 2))

    # Loop through all pairs of molecules
    for i in range(num_molecules):
        for j in range(num_molecules):
            if i == j:
                continue

            # Calculate the distance between the two molecules
            r = positions[i] - positions[j]

            # Implement periodic boundary conditions
            r[r > 5] -= 10
            r[r < -5] += 10

            # Calculate the acceleration of molecule i due to molecule j using the Leonard-Jones potential
            acceleration = 24 * epsilon / sigma * (2 * (sigma / np.linalg.norm(r))**13 - (sigma / np.linalg.norm(r))**7) * r / np.linalg.norm(r)
            accelerations[i] += acceleration

    return accelerations

num_molecules = 100
# Set the initial positions and velocities for the molecules
positions = np.random.uniform(-5, 5, size=(num_molecules, 2))
velocities = np.random.normal(0, 1, size=(num_molecules, 2))

# Set the timestep and number of steps to simulate
dt = 0.001
num_steps = 100

# Set the constants for the Leonard-Jones potential
sigma = 1
epsilon = 1

# Initialize an array to store the velocities of the molecules
velocities_array = np.zeros((num_steps, num_molecules, 2))

# Loop through the simulation steps
for i in range(num_steps):
    # Calculate the acceleration of each molecule using the Leonard-Jones potential
    accelerations = calc_acceleration(positions, sigma, epsilon)

    # Use the Verlet algorithm to update the positions and velocities
    positions = positions + dt * velocities + 0.5 * dt**2 * accelerations
    velocities = velocities + 0.5 * dt * (accelerations + calc_acceleration(positions, sigma, epsilon))

    # Implement periodic boundary conditions
    positions[positions > 5] -= 10
    positions[positions < -5] += 10

    # Store the velocities of the molecules in the array
    velocities_array[i] = velocities

# Calculate the histogram of the velocity distribution
hist, bins = np.histogram(velocities_array, bins=50)

# Plot the velocity distribution
plt.bar(bins[:-1], hist, width=bins[1]-bins[0])
plt.xlabel('Velocity')
plt.ylabel('Number of Molecules')
plt.show()
print(1)