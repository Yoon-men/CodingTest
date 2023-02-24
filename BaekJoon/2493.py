# 백준2493 : 탑
import sys; input = sys.stdin.readline

N = int(input())
Li = [(num+1, height) for num, height in enumerate(list(map(int, input().split())))]

ansLi = [0] * N
stack = []
for i in range(N) : 
    while stack : 
        if stack[-1][1] > Li[i][1] : 
            ansLi[i] = stack[-1][0]
            break
        stack.pop()
    stack.append(Li[i])

print(*ansLi)