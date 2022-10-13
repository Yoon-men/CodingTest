# 백준17352 : 여러분의 다리가 되어 드리겠습니다!
import sys ; input = sys.stdin.readline

def find(p, x) : 
    if p[x] != x : 
        p[x] = find(p, p[x])
    return p[x]

def union(p, x, y) : 
    x, y = find(p, x), find(p, y)
    if x < y : p[y] = x
    else : p[x] = y

if __name__ == "__main__" : 
    N = int(input())
    p = [i for i in range(N+1)]
    for _ in range(N-2) : 
        a, b = map(int, input().split())
        union(p, a, b)
    ans = []
    for i in range(1, N+1) : 
        if i == p[i] : ans.append(i)
    print(*ans)