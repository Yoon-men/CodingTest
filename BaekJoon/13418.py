# 백준13418 : 학교 탐방하기
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, graph: List[List[Tuple[int, int]]]) -> int : 
    def getFatigue(best_case: int) -> int : 
        cnt = 0

        visited = [0] * (N+1)
        hq = [(0, 0)]
        while hq : 
            w, u = heappop(hq)
            if not visited[u] : 
                if w : 
                    cnt += 1
                visited[u] = 1
                for v, w in graph[u] : 
                    heappush(hq, (w if best_case else -w, v))

        return cnt**2

    
    best, worst = getFatigue(best_case=1), getFatigue(best_case=0)

    return worst - best



if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M+1) : 
        A, B, C = map(int, input().split())
        C = bool(C)
        graph[A].append((B, 0 if C else 1))
        graph[B].append((A, 0 if C else 1))

    print(joyGo(N, graph))