import numpy as np
from solvers import Newton, Root, Bisection, Secant

# Solve the equation f(x) = cos(x) - x = 0 using Newton's method
# Define the function and its derivative
f = lambda x: np.cos(x) - x
df = lambda x: -np.sin(x) - 1

# Initialise the initial guess and tolerance
x0 = 0.5
tol = 1e-10

# Call the Newton's method function and compare to x ≃ 0.7390851332.
x_provided = 0.7390851332
x_Newton = Newton(f, df, x0, tol)
x_Bisection = Bisection(f, -1, 1, tol)
x_Secant = Secant(f, -1, 1, tol)
x_Root = Root(f, x0)

print('Solutions to f(x) = cos(x) - x = 0:')
print('Provided solution:         x =', x_provided)
print('Newton\'s method solution:  x =', x_Newton)
print('Bisection method solution: x =', x_Bisection)
print('Secant method solution:    x =', x_Secant)
print('Root method solution:      x =', x_Root)