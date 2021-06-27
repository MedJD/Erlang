from decimal import Decimal
from math import factorial
import json

def sum(A, N):
    i = 0
    s = Decimal(0.0)

    while i <= N:
        s+= A**i / Decimal(factorial(i))
        i+= 1

    return s

def erlangB(A, N):
    res = (A**N / factorial(int(N))) / sum(A, N)
    return res


def generate_traffic_file(minN, maxN, minA, maxA, stepA):
    data = {}

    N = Decimal(minN)            
    while N <= maxN:            
        A = Decimal(minA)       
        data = {}
        while A <= maxA:        
            B = erlangB(A=A, N=N)
            data["{:.4f}".format(B)] = "{:.2f}".format(A)
            print(N, "{:.2f}".format(A))
            A+= Decimal(stepA)
        with open('traffic/traffic_N=' + str(N), 'w+') as file:
            file.write(json.dumps(data))
        N+= 1

if __name__ == '__main__':
    minN = 1
    maxN = 220
    minA = 0.01
    maxA = 200
    stepA = 0.01
    generate_traffic_file(minN, maxN, minA, maxA, stepA)