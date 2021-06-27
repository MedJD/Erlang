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


def generate_traffic_file():
    data = {}
    #134 199.71

    N = Decimal(195)

    while N <= 220:
        A = Decimal(0.01)
        data = {}
        while A <= 200:
            B = erlangB(A=A, N=N)
            data["{:.4f}".format(B)] = "{:.2f}".format(A)
            print(N, "{:.2f}".format(A))
            A+= Decimal(0.01)
        with open('data/ErlangB/traffic/traffic_N=' + str(N), 'w+') as file:
            file.write(json.dumps(data))
        N+= 1

def get_traffic(B, N):
    with open('data/ErlangB/traffic/traffic_N=' + str(N), 'r') as file:
        data = json.loads(file.read())

        correct = 0
        while correct < 0.002:
            try:
                res = float(data["{:.4f}".format(B+correct)])
                break
            except:
                correct += 0.0001
                continue
        return "{:.2f}".format(res)

def get_proba(A, N):
    return erlangB(A=A, N=N)

if __name__ == '__main__':
    # calculate_traffic()
    #print(get_traffic(B=0.5, N=5))
    generate_traffic_file()
