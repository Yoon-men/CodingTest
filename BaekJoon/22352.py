# 백준22352 : 항체 인식
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(N: int, M: int, before_graph: List[List[int]], after_graph: List[List[int]]) -> str: 
    def BFS(a: int, b: int) -> str: 
        before_change = before_graph[a][b]
        before_graph[a][b] = after_graph[a][b]

        dq = deque([(a, b)])
        while dq: 
            x, y = dq.popleft()
            for i in range(4): 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < M): 
                    if before_graph[nx][ny] == before_change: 
                        before_graph[nx][ny] = before_graph[x][y]
                        dq.append((nx, ny))
        
        return "YES" if (before_graph == after_graph) else "NO"


    dx, dy = (-1,1,0,0), (0,0,1,-1)

    for i in range(N): 
        for j in range(M): 
            if before_graph[i][j] != after_graph[i][j]: 
                return BFS(i, j)

    return "YES" if (before_graph == after_graph) else "NO"



if __name__ == "__main__": 
    N, M = map(int, input().split())
    before_graph = [list(map(int, input().split())) for _ in range(N)]
    after_graph = [list(map(int, input().split())) for _ in range(N)]

    print(joyGo(N, M, before_graph, after_graph))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, before_graph, after_graph, ans"),
    [
        (1, 4, 4, [[2, 2, 2, 1], [2, 2, 1, 3], [2, 1, 3, 3], [1, 3, 3, 3]], [[4, 4, 4, 1], [4, 4, 1, 3], [4, 1, 3, 3], [1, 3, 3, 3]], "YES"), 
        (2, 4, 4, [[2, 2, 2, 1], [2, 2, 1, 3], [2, 1, 3, 3], [1, 3, 3, 3]], [[2, 2, 2, 1], [2, 2, 1, 3], [2, 1, 3, 3], [1, 3, 3, 3]], "YES"), 
        (3, 4, 4, [[2, 2, 2, 1], [2, 2, 1, 3], [2, 1, 3, 3], [1, 3, 3, 3]], [[2, 2, 2, 1], [2, 2, 2, 3], [2, 1, 3, 3], [1, 3, 3, 3]], "YES"), 
        (4, 4, 4, [[2, 2, 2, 1], [2, 2, 1, 2], [2, 1, 2, 2], [1, 2, 2, 2]], [[3, 3, 3, 1], [3, 3, 1, 3], [3, 1, 3, 3], [1, 3, 3, 3]], "NO"), 
        (5, 3, 5, [[1, 1, 1, 3, 3], [1, 1, 2, 3, 3], [1, 1, 2, 2, 4]], [[1, 1, 1, 4, 4], [1, 1, 2, 4, 4], [1, 1, 2, 2, 4]], "YES"), 
        (6, 2, 2, [[1, 1], [1, 2]], [[2, 1], [1, 2]], "NO")
    ]
)

def test_joyGo(case_num: int, N: int, M: int, before_graph: List[List[int]], after_graph: List[List[int]], ans: str) -> None: 
    res = joyGo(N, M, before_graph, after_graph)
    assert res == ans, f"Test Case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ