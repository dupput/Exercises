import numpy as np

# The Moore–Penrose inverse, or pseudoinverse, provides a means to define the inverse of
# singular and non-square matrices. For a matrix A with linearly independent columns, the
# pseudoinverse is defined as A+ = (AT * A)^−1 * AT , where AT is the transpose of A

# (a) Write a Python function that returns the pseudoinverse of a matrix A.

def pseudoinverse(A):
    # Compute the transpose of A
    A_transpose = np.transpose(A)

    # Compute the inverse of A_transpose * A
    inverse = np.linalg.inv(np.dot(A_transpose, A))

    # Compute the pseudoinverse
    pseudoinverse = np.dot(inverse, A_transpose)

    return pseudoinverse


# b) Consider the matrix A = [[1 -1] [2 4] [1 1] [3 8]]
# Compute A+ * A and show that this is equal to I, the identity matrix.

A = np.array([[1, -1], [2, 4], [1, 1], [3, 8]])

# Compute A+ * A
product = np.dot(pseudoinverse(A), A)

# Print the result with 2 decimal places
print(np.round(product, 2))

# (c) Now consider the over-determined system of linear equations given by
# [[1 -1] [2 4] [1 1] [3 8]] * [[x1] [x2]] = [[2] [4] [6] [8]]

# Use the pseudoinverse to compute the solution x. Hint: left multiply the system of
# equations Ax = b by A+ and use A+A = I to show that x = A+b.

# Create the matrix A
A = np.array([[1, -1], [2, 4], [1, 1], [3, 8]])

# Create the vector b
b = np.array([2, 4, 6, 8])

# Compute the solution x: A+ * A * x = A+ * b => x = A+ * b
x = np.dot(pseudoinverse(A), b)

# Print the solution x
print(x)

# It should come as a surprise that you are able to compute x because over-determined
# systems of equations usually do not have a solution. Indeed, performing Gaussian
# elimination will show that there is no vector x∗ that solves the linear system (3). So,
# what does the vector x = A+b correspond to then? It is the closest approximation to
# the vector x∗ that would solve (3). More specifically, the vector x = A+b minimises
# the error ||Ax − b||, where || · || is the Euclidean norm. Minimising ||Ax − b|| is known
# as a least-squares problem.

# Calculate the error ||Ax - b||
error = np.linalg.norm(np.dot(A, x) - b)

# Print the error
print(error)