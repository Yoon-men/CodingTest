# 백준30024 : 옥수수밭
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, M: int, graph: List[List[int]], K: int) -> List[Tuple[int, int]]: 
    visited = [[0] * M for _ in range(N)]
    
    hq = []
    for i in range(N): 
        for j in range(M): 
            if (i == 0 or i == N-1) or (j == 0 or j == M-1): 
                heappush(hq, (-graph[i][j], i, j))
                visited[i][j] = 1
    
    dx, dy = [-1,1,0,0], [0,0,1,-1]
    corn_list = [0] * K

    for i in range(K): 
        _, x, y = heappop(hq)
        corn_list[i] = (x+1, y+1)

        for j in range(4): 
            nx, ny = x+dx[j], y+dy[j]
            if (0 <= nx < N) and (0 <= ny < M) and (not visited[nx][ny]): 
                heappush(hq, (-graph[nx][ny], nx, ny))
                visited[nx][ny] = 1

    return corn_list

    ### ----- joyGo() end ----- ###


if __name__ == "__main__": 
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())
    
    ans = joyGo(N, M, graph, K)
    for row in ans: 
        print(*row)


# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, graph, K, ans"), 
    [
        (
            1, 
            4, 5, [[1, 18, 2, 3, 4], [12, 17, 15, 20, 5], [11, 14, 19, 13, 6], [10, 9, 16, 8, 7]], 6, 
            [(1, 2), (2, 2), (4, 3), (3, 3), (2, 3), (2, 4)]
        ), 
        (
            2, 
            3, 3, [[9, 8, 1], [4, 5, 2], [6, 3, 7]], 4, 
            [(1, 1), (1, 2), (3, 3), (3, 1)]
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, graph: List[List[int]], K: int, ans: List[Tuple[int, int]]) -> None: 
    res = joyGo(N, M, graph, K)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ