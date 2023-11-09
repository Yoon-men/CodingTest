# 백준1414 : 불우이웃돕기
import sys; input = sys.stdin.readline
from typing import List
from heapq import heappush, heappop

def joyGo(N: int, board: List[List[str]]) -> int: 
    for i in range(N): 
        for j in range(N): 
            board[i][j] = ord(board[i][j]) - (96 if (board[i][j].islower()) else 48 if (board[i][j] == '0') else 38)
    
    graph = [[] for _ in range(N)]
    for i in range(N): 
        for j in range(N): 
            if board[i][j] == 0: continue
            graph[i].append((j, board[i][j]))
            graph[j].append((i, board[i][j]))

    ans = 0
    hq = [(0, 0)]
    visited = [0] * N
    while hq: 
        w, u = heappop(hq)
        if not visited[u]: 
            visited[u] = 1
            ans += w
            for v, w in graph[u]: heappush(hq, (w, v))
    
    all_length = 0
    for row in board: all_length += sum(row)

    return -1 if (sum(visited) != N) else all_length - ans

    

if __name__ == "__main__": 
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    
    print(joyGo(N, board))