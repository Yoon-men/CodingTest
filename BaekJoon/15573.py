# 백준15573 : 채굴
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(N: int, M: int, K: int, graph: List[List[int]]) -> int: 
    def bfs(strength: int) -> int: 
        dx, dy = [-1,1,0,0], [0,0,1,-1]

        visited = [[0 for _ in range(M)] for _ in range(N)]
        dq = deque([(0, 0)])
        visited[0][0] = 1

        cnt = 0
        while dq: 
            x, y = dq.popleft()
            if graph[x][y]: 
                cnt += 1

            for i in range(4): 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < M) and (not visited[nx][ny]): 
                    if graph[nx][ny] <= strength: 
                        dq.append((nx, ny))
                        visited[nx][ny] = 1
        
        return cnt

        ### ----- bfs() end ----- ###

    N += 1
    M += 2
    graph = [[0] * M] + [[0] + row + [0] for row in graph]

    s, e = 0, 10**6
    while s <= e: 
        m = (s + e) // 2
        if bfs(m) < K: 
            s = m + 1
        else: 
            e = m - 1
    
    return s

    ### ----- joyGo() end ----- ###



if __name__ == "__main__": 
    N, M, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    print(joyGo(N, M, K, graph))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, K, graph, ans"), 
    [
        (
            1, 
            5, 5, 10, 
            [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 2, 2, 3], [3, 2, 2, 2, 3], [3, 2, 2, 2, 3]], 
            3
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, K: int, graph: List[List[int]], ans: int) -> None: 
    res = joyGo(N, M, K, graph)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ