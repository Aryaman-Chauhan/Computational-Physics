import numpy as np

# Set the size of the domain
N = 100

# Set the boundary conditions
u = np.zeros((N, N))
u[:, 1] = 1.0
u[:, -1] = -1.0
u[1, :] = 1.0
u[-1, :] = -1.0

# Set the initial guess for the solution
u_new = np.zeros((N, N))

# Set the convergence tolerance
tol = 1e-6

# Perform the Jacobi relaxation
while True:
  # Update the solution at each grid point in turn
  for i in range(1, N-1):
    for j in range(1, N-1):
      u_new[i, j] = (u[i-1, j] + u[i+1, j] + u[i, j-1] + u[i, j+1]) / 4.0

  # Check for convergence
  if np.max(np.abs(u_new - u)) < tol: # type:ignore
    break

  # Update the solution
  u = u_new

# Plot the solution
import matplotlib.pyplot as plt
plt.imshow(u)
# plt.plot(u)
plt.show()
