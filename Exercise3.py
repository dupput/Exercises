import numpy as np

# Create a numpy array
a = np.array([5,4,9,2,0,4,7,2])
print(a)

# (a) Print the last entry of a.
print(a[-1])

# (b) Print the values of a[1:6] and explain the output. Now try printing the values of
# a[:-2] and a[::2]. What do these do?

# Print the values of a[1:6]
print(a[1:6])
print('The output is the values of a from index 1 to 5.')

# Print the values of a[:-2]
print(a[:-2])
print('The output is the values of a from index 0 to the second last index.')

# Print the values of a[::2]
print(a[::2])
print('The output is the values of a from index 0 to the last index with a step size of 2.')

# (c) Change the last entry of a to −9 and print the result. Now run the command a[0:3] = 1 
# and print the result. How has this altered a?
a[-1] = -9
print(a)

a[0:3] = 1
print(a)

print('The last entry of a has been changed to -9 and the first 3 entries of a have been changed to 1.')



