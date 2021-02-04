# Solving Using PySMT
## solver.py
* Usage: python3 solver.py < ${testcase}
* Complexity of Implementation of Adding Constraint
    * In the following analysis, let $\hat{K}$ be the total number of services demanded. Note that $\hat{K} \leq I \times K$ since not all services are demanded by all vehicles.
    * Equation 1: $O(\hat{K}^2)$ 
    * Equation 2: $O(\hat{K})$ 
    * Equation 3: $O(\hat{K})$ 
    * Equation 4: $O(\hat{K})$ 
    * Equation 5: $O(\hat{K})$ 
    * Equation 6: $O(\hat{K})$ 
    * Equation 7: $O(J \times T \times \hat{K})$
      * The implementation of Equation 7 involves indicator variable

## testcase_parser.py
* Usage: python3 testcase_parser.py < ${testcase}
* Prints testcase in a (hopefully) more human-readable way

## testcase_generator.py
* Generates testcases given user-supplied parameters (the range of variables). It creates testcase by generating a random testcase and solve it using `solver.py`. Once the testcase is SAT (i.e. solvable), the testcase is saved.

## time_record.py
* A not-so-modularized script to test the computation time of `solver.py`. To be further reused, it should be modularized.

## tile_plot.py
* A not-so-modularized script to plot the result of `time_record.py`. To be further reused, it should be modularized, and it could be combined into `time_record.py`.