from random import randrange, choices
from pandas import *
import solver
import os
import os
import time

# Input ========================================================================
I_range = [4, 5]
J_range = [4, 5]
K_range = [5,6]
T_range = [0, 5]
C_range = [1, 6]
Tv_range = [1, 3]
D_range = [10, 180] # or -1 
F_range = [8, 30] # or -1
M_range = [0, 100]
M_bar_range = [100, 700]
file_names = ["testcases/09"] # with suffix .in

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

    print(f"$I = {I}$, $J = {J}$, $K = {K}$, $T_{{max}}={T_MAX}$")

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
            for t in range(0, T_MAX):
                # f.write("1 ")
               f.write(f"{choices([0, 1], weights=(3, 7))[0]} ")
            #for t in range(0, T_MAX-2):
            #    f.write("0 ")
            #if j == 0:
            #    f.write("0 0 ")
            #else:
            #    f.write("0 1 ")
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
    for fn in file_names:
        count = 0
        while True:
            print(f"Trying to generate {fn}.in for the {count}-th attempt")
            generate_temp_file()
            start_time = time.time()
            os.system("timeout 7200 python3 solver.py < temp.in > temp.out")
            end_time = time.time()
            f = open("temp.out", "r")
            print(f"time: {end_time - start_time}")
            output = f.readline()
            f.close()
            print(len(output))
            if len(output) != 0 and output != "Unsat\n": # and output != "Objective value: 0\n":
                os.system(f"mv temp.in {fn}.in; rm temp.out;")
                break
            count = count + 1

if __name__ == "__main__":
    main()

    

