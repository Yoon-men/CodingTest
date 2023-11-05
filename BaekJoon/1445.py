# 백준1445 : 일요일 아침의 데이트
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, M: int, _map: List[List[str]]) -> Tuple[int, int] : 
    def findPoint() -> Tuple[int, int, int, int] : 
        start_x, start_y, final_x, final_y = -1, -1, -1, -1
        for i in range(N) : 
            for j in range(M) : 
                if _map[i][j] == 'S' : start_x, start_y = i, j
                elif _map[i][j] == 'F' : final_x, final_y = i, j

                if all(point > -1 for point in (start_x, start_y, final_x, final_y)) : return (start_x, start_y, final_x, final_y)


    def isNearGarbage(x: int, y: int) -> int : 
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and (_map[nx][ny] == 'g') : 
                return 1

        return 0


    dx, dy = [-1,1,0,0], [0,0,1,-1]

    start_x, start_y, final_x, final_y = findPoint()
    visited = [[-1] * M for _ in range(N)]
    visited[start_x][start_y] = 1

    queue = [(0, 0, start_x, start_y)]
    while queue : 
        cross_garbage_cnt, near_garbage_cnt, x, y = heappop(queue)
        if (x == final_x) and (y == final_y) : return (cross_garbage_cnt, near_garbage_cnt)

        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == -1) : 
                visited[nx][ny] = 1

                if _map[nx][ny] == 'g' : 
                    heappush(queue, (cross_garbage_cnt+1, near_garbage_cnt, nx, ny))
                elif _map[nx][ny] == '.' : 
                    heappush(queue, (cross_garbage_cnt, near_garbage_cnt + isNearGarbage(nx, ny), nx, ny))
                elif (_map[nx][ny] == 'S') or (_map[nx][ny] == 'F') : 
                    heappush(queue, (cross_garbage_cnt, near_garbage_cnt, nx, ny))



if __name__ == "__main__" : 
    N, M = map(int, input().split())
    _map = [list(input().strip()) for _ in range(N)]

    print(*joyGo(N, M, _map))