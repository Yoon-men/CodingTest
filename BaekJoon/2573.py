# 백준2573 : 빙산
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(N: int, M: int, graph: List[List[int]]) -> int: 
    def bfs(start_x: int, start_y: int) -> None: 
        dx, dy = [-1,1,0,0], [0,0,1,-1]

        dq = deque([(start_x, start_y)])
        visited[start_x][start_y] = 1

        while dq: 
            x, y = dq.popleft()
            for i in range(4): 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < M): 
                    # 근처의 바닷물
                    if graph[nx][ny] == 0: 
                        visited[x][y] += 1
                    # 근처의 빙하
                    elif (not visited[nx][ny]) and (graph[nx][ny] > 0): 
                        dq.append((nx, ny))
                        visited[nx][ny] = 1


    year = 0

    while True: 
        visited = [[0] * M for _ in range(N)]
        cnt = 0

        # 빙하 방문
        for i in range(N): 
            for j in range(M): 
                if (graph[i][j]) and (not visited[i][j]): 
                    bfs(i, j)
                    cnt += 1

        # 빙하가 녹고 있어요
        for i in range(N): 
            for j in range(M): 
                if visited[i][j]: 
                    graph[i][j] -= (visited[i][j] - 1)
                    if graph[i][j] < 0: graph[i][j] = 0

        
        year += 1
        if cnt == 0: return 0
        elif cnt >= 2: return year-1



if __name__ == "__main__": 
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    print(joyGo(N, M, graph))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("N, M, graph, ans"), 
    [
        (5, 7, [[0, 0, 0, 0, 0, 0, 0], [0, 2, 4, 5, 3, 0, 0], [0, 3, 0, 2, 5, 2, 0], [0, 7, 6, 2, 4, 0, 0], [0, 0, 0, 0, 0, 0, 0]], 2)
    ]
)

def test_joyGo(N: int, M: int, graph: List[List[int]], ans: int) -> None: 
    res = joyGo(N, M, graph)
    assert res == ans, f"Test case - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ