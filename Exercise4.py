import numpy as np

# (a) Create a NumPy array r that contains 20 random numbers between 1 and 9 that
# from a uniform distribution. Print the result.

r = np.random.uniform(1, 10, 20)
print(r)

# (b) Logical indexing provides a quick way to access and modify entries in a NumPy
# array that satisfy certain criteria. In this question, we’ll use logical indexing to
# replace all of the entries in r that are smaller than 5 with 0. First, run the command
# idx = r < 5. Print the value of idx. Explain the result you see. Now run the
# command r[idx] = 0 and print the value of r. What has happened?

idx = r < 5
print(idx)
print('The result is a list of True and False values. The True values are the indices of the elements in r that are less than 5.')

r[idx] = 0
print(r)
print('The elements in r that are less than 5 have been changed to 0.')