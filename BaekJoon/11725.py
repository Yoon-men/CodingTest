# 백준11725 : 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n) : 
    for i in graph[n-1] : 
        if answerLi[i-1] == 0 : 
            answerLi[i-1] = n
            dfs(i)

if __name__ == "__main__" : 
    N = int(input())
    graph = [[] for _ in range(N)]
    answerLi = [0] * N      # == visited
    for _ in range(N-1) : 
        A, B = map(int, input().split())
        graph[A-1].append(B)
        graph[B-1].append(A)
    dfs(1)
    for i in answerLi[1:] : 
        print(i)