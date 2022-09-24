# 백준7511 : 소셜 네트워킹 어플리케이션
import sys ; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(p, x) : 
    if p[x] != x : 
        p[x] = find(p, p[x])
    return p[x]

def union(p, x, y) : 
    x, y = find(p, x), find(p, y)
    if x < y : p[y] = x
    else : p[x] = y

if __name__ == "__main__" : 
    for i in range(int(input())) : 
        n = int(input())
        p = [i for i in range(n)]
        for j in range(int(input())) : 
            a, b = map(int, input().split())
            if find(p, a) != find(p, b) : union(p, a, b)
        print(f"Scenario {i+1}:")
        for _ in range(int(input())) : 
            u, v = map(int, input().split())
            print(0 if find(p, u) != find(p, v) else 1)
        print()