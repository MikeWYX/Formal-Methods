from z3 import *
import time
start_time = time.time()
N = 8
s = Solver()
board = [[Bool(f"Q_{i}_{j}") for j in range(N)] for i in range(N)]
# At least one queen on row i
for i in range(N):
    s.add(Or([board[i][j] for j in range(N)]))
# At most one queen on row i
for i in range(N):
    for j in range(N):
        for k in range(j+1, N):
            s.add(Or(Not(board[i][j]), Not(board[i][k])))
# At least one queen on column j
for j in range(N):
    s.add(Or([board[i][j] for i in range(N)]))
# At most one queen on column j
for j in range(N):
    for i in range(N):
        for k in range(i+1, N):
            s.add(Or(Not(board[i][j]), Not(board[k][j])))
# Diagonal constraints
for i in range(N):
    for j in range(N):
        for k in range(1, N):
            if i+k < N and j+k < N:
                s.add(Or(Not(board[i][j]), Not(board[i+k][j+k])))
            if i+k < N and j-k >= 0:
                s.add(Or(Not(board[i][j]), Not(board[i+k][j-k])))
print(s.check())
print(s.model())
end_time = time.time()
running_time = end_time - start_time
print("Running time:", running_time, "seconds")


