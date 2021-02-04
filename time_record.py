from random import randrange
from pandas import *
import solver
import os
import time

# Input ========================================================================
# I_range = [6,7]
# J_range = [4,5]
# K_range = [4,5]
# T_range = [0, 5]
# C_range = [1, 5]
# Tv_range = [1, 3]
# D_range = [10, 11] # or -1 
# F_range = [0, 20] # or -1
# M_range = [0, 100]
# M_bar_range = [800, 1000]
# file_names = ["testcases/06", "testcases/06", "testcases/06"] # with suffix .in

# times = []

def generate_temp_file():
    # Generate random
    # T = [[randrange(0, T_MAX) for k in range(0, K)] for j in range(0, J)]
    # C = [[randrange(0, T_MAX) for k in range(0, K)] for j in range(0, J)]
    # Tv = [[[randrange(0, T_MAX) if j != jj else 0 for k in range(0, K)] for jj in range(0, J)] for j in range(0, J)]
    # D = [[randrange(-1, J) for k in range(0, K)] for i in range(0, I)]
    # F = [[-1 if D[j][k] == -1 else randrange(1, J) for k in range(0, K)] for j in range(0, J)]
    # R = [[[randrange(0, 2) for t in range(0, T_MAX)] for j in range(0, J)] for i in range(0, I)]
    # M = [randrange(0, M_MAX) for k in range(0, K)]
    # M_bar = [randrange(0, M_MAX) for j in range(0, J)]
    I = randrange(I_range[0], I_range[1])
    J = randrange(J_range[0], J_range[1])
    K = randrange(K_range[0], K_range[1])
    # D is generated first to determine T_MAX
    D = []
    T_MAX = -1
    while T_MAX <= 0:
        D.clear()
        for i in range(0, I):
            D.append([])
            for k in range(0, K):
                if randrange(0, 2) == 0:
                    D[-1].append(-1)
                else:
                    D[-1].append(randrange(D_range[0], D_range[1]))
                T_MAX = max(T_MAX, D[-1][-1])

    print(f"I:{I}, J:{J}, K:{K}, T_MAX:{T_MAX}")

    f = open("temp.in", "w")
    # I
    f.write(f"{I}\n")
    # J
    f.write(f"{J}\n")
    # K
    f.write(f"{K}\n")
    # T_MAX
    f.write(f"{T_MAX}\n")
    # T
    for j in range(0, J):
        for k in range(0, K):
            f.write(f"{randrange(T_range[0], T_range[1])} ")
        f.write("\n")
    # C
    for j in range(0, J):
        for k in range(0, K):
            f.write(f"{randrange(C_range[0], C_range[1])} ")
        f.write("\n")
    # Tv
    for j in range(0, J):
        for jj in range(0, J):
            for k in range(0, K):
                if(j == jj):
                    f.write("0 ")
                else:
                    f.write(f"{randrange(Tv_range[0], Tv_range[1])} ")
            f.write("\n")
    # D
    for i in range(0, I):
        for k in range(0, K):
            f.write(f"{D[i][k]} ")
        f.write("\n")
    # F
    for i in range(0, I):
        for k in range(0, K):
            if D[i][k] == -1:
                f.write("-1 ")
            else:
                f.write(f"{randrange(F_range[0], F_range[1])} ")
        f.write("\n")
    # R
    for i in range(0, I):
        for j in range(0, J):
            for k in range(0, K):
                f.write(f"{randrange(0, 2)} ")
            # for k in range(0, K-2):
            #     f.write("0 ")
            # if j == 0:
            #     f.write("0 0 ")
            # else:
            #     f.write("0 1 ")
            f.write("\n")
    # M
    for k in range(0, K):
        f.write(f"{randrange(M_range[0], M_range[1])} ")
    f.write("\n")
    # M_bar
    for j in range(0, J):
        f.write(f"{randrange(M_bar_range[0], M_bar_range[1])} ")
    f.close()

def main():
    x = 0
    for fn in file_names:
        count = 0
        while True:
            print(f"Trying to generate {fn}.in for the {count}-th attempt")
            generate_temp_file()
            start_time = time.time()
            os.system("python3 solver.py < temp.in > temp.out")
            end_time = time.time()
            f = open("temp.out", "r")
            output = f.readline()
            f.close()
            if output != "Unsat\n":
                print(f"time: {end_time - start_time}")
                x += end_time - start_time
                os.system(f"mv temp.in {fn}.in; rm temp.out;")
                break
            count = count + 1
    return x / 3

if __name__ == "__main__":
    # ll = [[[2,3],[2,3]], [[2,3],[4,5]],[[4,5], [2,3]], [[2,3], [6,7]], [[4,5],[4,5]], [[6,7], [2,3]]]
    ll = [[[8,9],[8,9]]]
    KK = [[2,3]]
    T_range = [0, 5]
    C_range = [1, 5]
    Tv_range = [1, 3]
    D_range = [10, 11] # or -1 
    F_range = [0, 20] # or -1
    M_range = [0, 100]
    M_bar_range = [800, 1000]   
    file_names = ["testcases/06", "testcases/06", "testcases/06"] # with suffix .in
    times = {}
    for l in ll:
        [I_range, J_range] = l
        for K_range in KK:
            times[f"i={I_range[0]},j={J_range[0]}"] = main()
            print(times)


    

