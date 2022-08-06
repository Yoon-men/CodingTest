# 백준17299 : 오등큰수
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
answer = [-1] * N
stack = []

for i in range(N):
    while stack and (cnt[A[stack[-1]]] < cnt[A[i]]):
            answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)