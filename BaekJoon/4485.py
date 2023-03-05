# 백준4485 : 녹색 옷 입은 애가 젤다지?
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstraJoyGo(graph) : 
    N = len(graph)
    dx, dy = [-1,1,0,0], [0,0,1,-1]

    shitLi = [[sys.maxsize]*N for _ in range(N)]; shitLi[0][0] = 0
    que = [(graph[0][0], 0, 0)]
    
    while que : 
        shit, x, y = heappop(que)
        if (x == N-1) and (y == N-1) : return shitLi[x][y]

        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < N) : 
                total_shit = shit + graph[nx][ny]
                if total_shit < shitLi[nx][ny] : 
                    shitLi[nx][ny] = total_shit
                    heappush(que, (total_shit, nx, ny))


if __name__ == "__main__" : 
    cnt = 1

    while True : 
        N = int(input())
        if N == 0 : break

        graph = [list(map(int, input().split())) for _ in range(N)]

        print(f"Problem {cnt}: {dijkstraJoyGo(graph)}")
        cnt += 1