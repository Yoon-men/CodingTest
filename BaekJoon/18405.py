# 백준18405 : 경쟁적 전염
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(N: int, K: int, graph: list, S: int, X: int, Y: int) -> None : 
    def BFS(virus_list: list) -> list : 
        visited = graph
        dq = deque(virus_list)
        dx, dy = [-1,1,0,0], [0,0,1,-1]
        while dq : 
            virus, x, y, cnt = dq.popleft()
            if cnt == S : break
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]) : 
                    visited[nx][ny] = virus
                    dq.append((virus, nx, ny, cnt+1))
            cnt += 1

        return visited


    virus_list = sorted([(graph[i][j], i, j, 0) for i in range(N) for j in range(N) if graph[i][j]])
    ansLi = BFS(virus_list)

    print(ansLi[X-1][Y-1])



if __name__ == "__main__" : 
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split())
    joyGo(N, K, graph, S, X, Y)