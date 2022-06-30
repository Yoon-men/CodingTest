# 백준15829 : Hashing
import sys
input = sys.stdin.readline

L = int(input())
T = input().strip()
answer = 0

for i in range(L) : 
    answer += (ord(T[i])-96) * (31**i)

print(answer % 1234567891)