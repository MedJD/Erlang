from math import factorial
import json

def sum(A, N):
    i = 0
    s = 0.0

    while i <= N:
        s+= A**i / factorial(i)
        i+= 1

    return s

def erlangB(A, N):
    res = (A**N / factorial(int(N))) / sum(A, N)
    return res


def generate_traffic_file():
    data = {}
    N = 1

    while N <= 1000:
        A = 0.0
        while A <= 1000:
            data[str(N)] = {}
            res = erlangB(A=A, N=N)
            data[str(N)]["{:.4f}".format(A)] = res
            print(N, "{:.4f}".format(A))
            A+= 0.0001
        N+= 1

    with open('traffic', 'w') as file:
        file.write(json.dumps(data))

def get_traffic():
    with open('traffic', 'r') as file:
        data = json.loads(file.read())
        res = data['20']["{:.4f}".format(17.61)]*100
        print(res)

def get_proba(A, N):
    return erlangB(A=A, N=N)

if __name__ == '__main__':
    # calculate_traffic()
    # get_traffic()
    generate_traffic_file()