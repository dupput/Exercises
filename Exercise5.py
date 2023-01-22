import numpy as np

# Solve the linear system of equations Ax = b where
# A = [1 0 0 0, 1 −2 1 0, 0 1 −2 1, 0 0 0 1], b = [0 1 1 2]
# Print the solution x. Then compute Ax − b and print the result. Can you explain the values you see?

# Create the matrix A
A = np.array([[1, 0, 0, 0], [1, -2, 1, 0], [0, 1, -2, 1], [0, 0, 0, 1]])

# Create the vector b
b = np.array([0, 1, 1, 2])

# Solve the linear system of equations Ax = b
x = np.linalg.solve(A, b)
print(x)

# Compute Ax - b
print(np.dot(A, x) - b)
