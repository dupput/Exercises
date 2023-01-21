
# (a) Given two vectors in the form of two lists, e.g. ⃗ a = [1, 2, 3] and ⃗ b = [6, 5, 4], write a 
# Python function that returns the dot product of these vectors.

def dot_product(a, b):
    # Check if the two vectors are the same length
    if len(a) != len(b):
        print('Error: The two vectors are not the same length.')
        return None

    # Initialize the dot product
    dot_product = 0

    # Loop through the vectors and add the product of the corresponding elements
    for i in range(len(a)):
        dot_product += a[i] * b[i]

    return dot_product

a = [1, 2, 3]
b = [6, 5, 4]
print('The dot product of', a, 'and', b, 'is', dot_product(a, b), '.')

print('_____________________________________________\n')

# (b) Given two matrices in the form of nested lists (lists of lists), e.g. A = [[1, 2], [3, 4]],
# write a Python function that returns the product of these two matrices

def matrix_product(A, B):
    # Check if the number of columns in A is equal to the number of rows in B
    if len(A[0]) != len(B):
        print('Error: The number of columns in A is not equal to the number of rows in B.')
        return None

    # Initialize the product matrix
    C = []

    # Loop through the rows of A
    for i in range(len(A)):
        # Initialize the row of C
        row = []

        # Loop through the columns of B
        for j in range(len(B[0])):
            # Initialize the dot product
            dot_product = 0

            # Loop through the elements of the row of A and the column of B
            for k in range(len(A[0])):
                dot_product += A[i][k] * B[k][j]

            # Add the dot product to the row
            row.append(dot_product)

        # Add the row to the product matrix
        C.append(row)

    return C


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print('The product of', A, 'and', B, 'is', matrix_product(A, B), '.')

print('_____________________________________________\n')