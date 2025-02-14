from z3 import *
import time
start_time = time.time()
N = 8
Q = [ Int('Q_%i' % (i + 1)) for i in range(N) ]
val_c = [ And (1 <= Q[i], Q[i] <= N) for i in range(N) ]
col_c = [ Distinct (Q) ]
diag_c = [ If(i == j, True ,
And(i+Q[i]!=j+Q[j], i+Q[j]!=j+Q[i]))
for i in range(N) for j in range(i) ]
solve(val_c + col_c + diag_c)
end_time = time.time()
running_time = end_time - start_time
print("Running time:", running_time, "seconds")