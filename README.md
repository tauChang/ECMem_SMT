# Solving Using PySMT
## decision_solver.py
* Usage: python3 decisions_solver.py < ${testcase}
* Complexity of Implementation of Adding Constraint
    * In the following analysis, let $\hat{K}$ be the total number of services demanded. Note that $\hat{K} \leq I \times K$ since not all services are demanded by all vehicles.
    * Equation 1: $O(\hat{K}^2)$ 
    * Equation 2: $O(\hat{K})$ 
    * Equation 3: $O(\hat{K})$ 
    * Equation 4: $O(\hat{K})$ 
    * Equation 5: $O(\hat{K})$ 
    * Equation 6: $O(\hat{K})$ 
    * Equation 7: $O(J \times T \times \hat{K})$

## testcase_parser.py
* Usage: python3 testcase_parser.py < ${testcase}
* Prints testcase in a (hopefully) more human-readable way