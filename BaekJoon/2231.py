# 분해합
import sys
input = sys.stdin.readline
N = int(input())
for i in range(1, N + 1) : 
    num = list(map(int, str(i)))
    plus = i + sum(num)
    if plus == N : 
        print(i)
        break
    if i == N : 
        print(0)