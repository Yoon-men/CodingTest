# 백준17298 : 오큰수
import sys
input = sys.stdin.readline

N = int(input())
elements = list(map(int, input().split()))

answer = [-1] * N
stack = []

for i in range(N) : 
    while stack and elements[stack[-1]] < elements[i] : 
        answer[stack.pop()] = elements[i]
    stack.append(i)

print(*answer)