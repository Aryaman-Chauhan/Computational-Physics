import numpy as np
import matplotlib.pyplot as plt

def lj_force(r, sigma, epsilon):
    if r == 0:
        return 0
    elif r > 3:
        return 0
    else:
        return -4 * epsilon * (12 * (sigma / r)**12 - 6 * (sigma / r)**6) / r


def lj_acceleration(positions, masses, sigma = 1, epsilon = 1):
    num_particles = positions.shape[0]
    accelerations = np.zeros_like(positions)
    for i in range(num_particles):
        for j in range(num_particles):
            if i == j:
                continue
            r = np.linalg.norm(positions[i] - positions[j])
            force = lj_force(r, sigma, epsilon)
            accelerations[i] += force / masses[i]
    return accelerations

def verlet(positions, velocities, masses, dt):
    """
    Applies the Verlet algorithm to update the positions and velocities of a set of particles.
    """
    # Update positions
    positions += velocities * dt + 0.5 * np.expand_dims(masses * dt**2, axis=1)

    # Apply periodic boundary conditions
    positions = positions % L

    # Calculate new accelerations
    accelerations = np.zeros_like(positions)

    # Update velocities
    velocities += 0.5 * (accelerations + np.expand_dims(masses, axis=1)) * dt

def calc_velocity_distribution(velocities, masses, bin_size=0.1):
    """
    Calculates the velocity distribution of a set of particles.
    """
    # Calculate kinetic energies
    kinetic_energies = 0.5 * np.expand_dims(masses, axis=1) * velocities**2

    # Calculate speeds
    speeds = np.sqrt(2 * kinetic_energies / np.expand_dims(masses, axis=1))

    # Calculate histogram of speeds
    hist, edges = np.histogram(speeds, bins=np.arange(0, np.max(speeds)+bin_size, bin_size))

    # Normalize histogram
    hist = hist / np.sum(hist)

    return hist, edges

# Set parameters
num_particles = 1000
L = 10.0 # size of 2D space
T = 300.0 # temperature
masses = np.ones(num_particles) # masses of particles
dt = 0.01 # time step
num_steps = 1000 # number of time steps to simulate

# Initialize positions and velocities
positions = L * np.random.rand(num_particles, 2) # random initial positions
velocities = np.sqrt(np.repeat(T / masses, 2).reshape((num_particles, 2))) * np.random.randn(num_particles, 2) # random initial velocities

# Simulate time evolution
for i in range(num_steps):
    verlet(positions, velocities, masses, dt)

# Calculate velocity distribution
hist, edges = calc_velocity_distribution(velocities, masses)

# Calculate the histogram bin edges
bin_edges = np.histogram_bin_edges(velocities, bins='auto')

# Plot the histogram
plt.hist(velocities, bins=bin_edges, density=True)
plt.xlabel('Speed')
plt.ylabel('Probability density')
plt.show()

speeds = abs(velocities)
bin_edges = np.histogram_bin_edges(speeds, bins='auto')
plt.hist(speeds, bins=bin_edges, density=True)
plt.xlabel('Speed')
plt.ylabel('Probability density')
plt.show()

# print(hist)
# print(edges)
