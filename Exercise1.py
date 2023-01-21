import math


def LeibnizFormula(N):
    sum = 0
    for i in range(N):
        sum += 8/((4*i+1)*(4*i+3))

    return sum

# (a) Use this formula to compute approximations to π by taking N = 100, N = 1, 000, 
# and N = 10, 000.
N = 100
print(LeibnizFormula(N))

N = 1000
print(LeibnizFormula(N))

N = 10000
print(LeibnizFormula(N))