# Testcases
## Input Format
The first four lines contain four integers $I$, $J$, $K$, and $T_{max}$, indicating the number of vehicles, the number of servers, the number of services, and the upper bound of time (all time $\in [0, T_{max})$).

The next $J$ lines represents $T_{j, k}$. Each of these lines contains $K$ non-negative integers.

The next $J$ lines represents $C_{j, k}$. Each of these lines contains $K$ non-negative integers.

The following $J$ groups of $J$ lines represents $T^{\vee}_{j,j',k}$ (i.e. there are $J \times J$ lines). Each of these lines contains $K$ non-negative integers. The $k$-th integer in the $j'$-th line of the $j$-th group indicates the transmission time of $\sigma_k$  from $\epsilon_j$ to $\epsilon_{j'}$.

The next $I$ lines represents $D_{i, k}$. Each of these lines contains $K$ integers. The $k$-th integer of the $i$-th line is a non-negative integer if $\nu_i$ **DOES** demand $\sigma_k$, otherwise it will be -1.

The next $I$ lines represents $F_{i,k}$. Each of these lines contains $K$ non-negative integers.

The following $I$ groups of $J$ lines represents $R_{i, j, t}$ (i.e. there are $I \times J$ lines). Each of these lines contains $T_{max}$ integers that is either $0$ or $1$. The $t$-th integer of in the $j$-th line of the $i$-th group indicates if $\nu_i$ is in the communication of $\epsilon_j$ at time $t$.


The next line represents $M_{k}$. It contains $K$ non-negative integers.

The next line represents $\overline{M}_{j}$. It contains $J$ non-negative integers.

## Detail on Each Testcase
### 00.in
Generated manually. Objective value is 0.
### 01.in
Generated manually. Objective value is 5.
### 02.in
Generated automatically. Large $T_{max}$. Objective value is 0.
### 03.in 
Generated automaticallly. Large $T_{max}$. Objective value is 0.
### 04.in 
Generated automaticallly. Objective value is 18.
### 05.in
Generated automaticallly. Objective value is 19.
### 06.in
Generated automaticallly. $I = 7$, $J = 6$, $K = 3$, $T_{max}:135$. Objective value is 0.
### 07.in
Generated automaticallly. $I = 2$, $J = 2$, $K = 5$, $T_{max}:145$. Objective value is 0.
Time: 1598.0864915847778
### 08.in
Generated automatically. $I = 4$, $J = 2$, $K = 5$, $T_{max}=149$. Objective value is 0.
Time: 2645.628807783127
 
## Attempt Notes
* $I = 9$, $J = 11$, $K = 5$, $T_{max}=205$: killed by OS
* $I = 8$, $J = 12$, $K = 2$, $T_{max}=224$: 45hr not solved yet
