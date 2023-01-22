import numpy as np
from solvers import NewtonsMethod

# Newton’s method is a way of finding the solution x to nonlinear equations of the form
# f (x) = 0. For a single equation, Newton’s method works as follows. First, propose an
# initial guess of the solution x0. Then, create successive approximations to the solution
# using the recursive formula until |f (xn)| < ε, where ε is some user-defined tolerance (e.g. 10−10)
# In this exercise, you will create a Python module called solvers that contains code to
# run Newton’s method. You will then use a Python script to import the module and solve
# the equation f (x) = cos(x) − x = 0.

# (a) Create a Python file called solvers.py. This will be file for your module. In this
# file, write a Python function that implements Newton’s method using the recursive
# formula above. Note: your module should not run Newton’s method; this is what
# the script is for (see part (b)).

# (b) Create a Python script called main.py that: (i) imports your solvers module, (ii) has
# Python functions to evaluate f (x) and f ′(x), and (iii) calls the function for Newton’s
# method. Run your script to show that the solution to cos(x)−x is x ≃ 0.7390851332.

# (c) Solve the equation cos(x) − x using the root function in SciPy
