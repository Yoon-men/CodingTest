# 백준10870 : 피보나치 수 5
import sys
n = int(sys.stdin.readline())
fLi = [0, 1]                # Num of Fibonacci List
for i in range(2, n+1) : 
    fLi.append(fLi[i-2] + fLi[i-1])
print(fLi[n])