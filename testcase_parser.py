from pandas import *

def prettyprint(name, list_data):
    print(name + "\n")
    print(DataFrame(list_data))
    print("\n\n")

I = int(input())
J = int(input())
K = int(input())
T_MAX = int(input())

T = []
for j in range(0, J):
    T.append([])
    for val in [int(x) for x in input().split()]:
        T[-1].append(val)

C = []
for j in range(0, J):
    C.append([])
    for val in [int(x) for x in input().split()]:
        C[-1].append(val)

Tv = []
for j in range(0, J):
    Tv.append([])
    for jj in range(0, J):
        Tv[-1].append([])
        for val in [int(x) for x in input().split()]:
            Tv[-1][-1].append(val)

D = []
for i in range(0, I):
    D.append([])
    for val in [int(x) for x in input().split()]:
        D[-1].append(val)

F = []
for i in range(0, I):
    F.append([])
    for val in [int(x) for x in input().split()]:
        F[-1].append(val)

R = []
for i in range(0, I):
    R.append([])
    for j in range(0, J):
        R[-1].append([])
        for val in [int(x) for x in input().split()]:
            R[-1][-1].append(val)

M = [int(x) for x in input().split()]
M_bar = [int(x) for x in input().split()]

prettyprint("T_{j, k}", T)
prettyprint("C_{j, k}", C)
prettyprint("Tv_{j, j', k}", Tv)
prettyprint("D_{i, k}", D)
prettyprint("F_{i, k}", F)
prettyprint("R_{i, j, t}", R)
prettyprint("M_k", M)
prettyprint("Mbar_j", M_bar)

