import scipy as sp

def Newton(f, df, x0, tol):
    xn = x0
    while abs(f(xn)) >= tol:
        xn = xn - f(xn)/df(xn)
    return xn


def Root(f, x0):
    sol = sp.optimize.root(f, x0)
    return sol.x[0]


def Bisection(f, a, b, tol):
    if f(a)*f(b) > 0:
        print('Error: f(a) and f(b) must have opposite signs.')
        return None
    else:
        while abs(b-a) >= tol:
            c = (a+b)/2
            if f(a)*f(c) < 0:
                b = c
            else:
                a = c
        return (a+b)/2


def Secant(f, x0, x1, tol):
    while abs(x1-x0) >= tol:
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
    return x1