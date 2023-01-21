import math


# (a) Use this formula to compute approximations to π by taking N = 100, N = 1,000, and N = 10,000.
def LeibnizFormula(N):
    sum = 0
    for i in range(N):
        sum += 8/((4*i+1)*(4*i+3))

    return sum

N_100 = LeibnizFormula(100)
print('When N = 100, the approximation of pi is', N_100, '.')

N_1000 = LeibnizFormula(1000)
print('When N = 1000, the approximation of pi is', N_1000, '.')

N_10000 = LeibnizFormula(10000)
print('When N = 10000, the approximation of pi is', N_10000, '.')
print('_____________________________________________\n')

# (b) Given that π = 3.141592653589793..., what is the error of the approximation in each of these cases?
def Error(N):
    return abs(math.pi - LeibnizFormula(N))

print('The error of the approximation when N = 100 is', Error(100), '.')
print('The error of the approximation when N = 1000 is', Error(1000), '.')
print('The error of the approximation when N = 10000 is', Error(10000), '.')
print('_____________________________________________\n')

# (c) What value of N is needed to produce an error that is less than 10−7?
tol = 10e-7
N = 1
while Error(N) >= tol:
    # Increase N by a factor of the error divided by the tolerance
    factor = Error(N)/tol
    increment = math.ceil(N * math.log(factor) / 10)
    print('N =', N, 'Error =', Error(N), 'Increment =', increment, 'Factor =', factor)
    N += increment

print('The value of N needed to produce an error that is less than 10^-7 is', N, '.')