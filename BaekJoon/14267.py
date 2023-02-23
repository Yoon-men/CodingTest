# 백준14267 : 회사 문화 1
import sys; input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**9)

def DFS(master) : 
    for sergeant in relationDi[master] : 
        if not visited[sergeant] : 
            visited[sergeant] = 1
            ansLi[sergeant] += ansLi[master]
            DFS(sergeant)

if __name__ == "__main__" : 
    n, m = map(int, input().split())
    Li = list(map(int, input().split()))
    relationLi = [(sergeant+1, master-1) for sergeant, master in enumerate(Li[1:])]
    relationDi = defaultdict(list)
    for sergeant, master in relationLi : 
        relationDi[master].append(sergeant)
    ansLi = [0] * n
    for _ in range(m) : 
        person, compliment = map(int, input().split())
        ansLi[person-1] += compliment
    
    visited = [0] * n
    for i in range(1, n) : 
        DFS(i)

    print(*ansLi)