from decimal import Decimal
from math import factorial
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-A","--A",
                        help="Amount of traffic",
                        required=False,
                        type=float)

    parser.add_argument("-N","--N", 
                        help="Number of Channels",
                        required=False,
                        type=int)

    parser.add_argument("-B","--B",
					help="Blocking Probability as pourcent",
					required=False,
					type=float)

    args = parser.parse_args()
    return(args)

def verify_args():
    args = parse_args()

    nbr = 0
    if args.A != None:
        nbr+= 1
    if args.B != None:
        nbr+= 1
    if args.N != None:
        nbr+= 1
    if nbr != 2:
        print('Please give exactely two arguments')
        exit(0)

    return args


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

def get_traffic(B, N):
    with open('data/ErlangB/traffic/traffic_N=' + str(N), 'r') as file:
        data = json.loads(file.read())

        pair = 1
        correct = 0
        while True:
            try:
                A = float(data["{:.4f}".format(B+correct)])
                return float(A)
            except:
                if pair == 1:
                    correct*= -1
                    correct+= 0.0001
                    pair = -1
                else:
                    correct*= -1
                    pair = 1
                    correct += 0.0001
                continue

def get_proba(A, N):
    return erlangB(A=A, N=N)

def get_nbr_channel(A, B):
    correction = 0.0
    pair = 1
    while True:
        strA = "{:.2f}".format(A+correction)
        strB = "{:.4f}".format(B)
        N = 1
        while N <= 195:
            with open('data/ErlangB/traffic/traffic_N=' + str(N)) as file:
                content = file.readline()
                to_search = strB + '": "' + strA
                if to_search in content:
                    return(N)
            N+= 1
        if pair == 1:
            correction*= -1
            correction+= 0.01
            pair = -1
        else:
            correction*= -1
            pair = 1

if __name__ == '__main__':
    args = verify_args()

    if args.B == None:
        B = erlangB(A=Decimal(args.A), N=Decimal(args.N)) * 100
        B = "{:.4f}".format(B)
        print(f'B = {B}%')

    if args.A == None:
        A = get_traffic(B=args.B/100, N=args.N)
        print(f'A = {A} Erlangs')

    if args.N == None:
        N = get_nbr_channel(B=args.B/100, A=args.A)
        print(f'N = {N}')
