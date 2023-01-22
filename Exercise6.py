import numpy as np
import matplotlib.pyplot as plt

# (a) Use NumPy’s linspace function to create an array called t that contains 500 values
# between 0 and 5. Create a second array called y that stores the values of y = t^2 * e^−2t.
# Hint: use the exp function to compute the exponential of a NumPy array.

# Create the array t
t = np.linspace(0, 5, 500)

# Create the array y
y = t**2 * np.exp(-2*t)

# (b) Plot y as a function of x. Add labels to the x and y axes. Edit the line colour and
# thickness and font sizes to your preference.

# Plot y as a function of t
plt.plot(t, y, 'r', linewidth=2)

# Add labels to the x and y axes
plt.xlabel('t', fontsize=16)
plt.ylabel('y', fontsize=16)

plt.show()

# (c) Find the maximum value of y. Note: this is a simple way of finding the maximum
# of a function.

# Find the maximum value of y
max_y = np.max(y)
print(max_y)

# (d) Use logical indexing or otherwise to find the value of t at which y is maximal. Does
# this match up with what you see in your plot?

idx = y == max_y
max_t = t[idx]
print(max_t)

