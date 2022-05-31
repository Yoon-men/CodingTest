# 백준11399 : ATM
import sys
input = sys.stdin.readline

N = int(input())
time = sorted(list(map(int, input().split())))
answer = 0

for man in range(1, N+1) : 
    answer += sum(time[:man])
print(answer)