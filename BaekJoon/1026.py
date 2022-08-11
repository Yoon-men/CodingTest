# 백준1026 : 보물
import sys
input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))
answer = 0
for i in range(N) : 
    answer += A[i] * B[i]
print(answer)