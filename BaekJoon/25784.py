# 백준25784 : Easy-to-Solve Expressions
Li = sorted(list(map(int, input().split())))
A, B, C = Li
print(1 if (A+B == C) else 2 if (A*B == C) else 3)