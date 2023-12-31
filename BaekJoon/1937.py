# 백준1937 : 욕심쟁이 판다
import sys; input = sys.stdin.readline
from typing import List
sys.setrecursionlimit(10**6)

def joyGo(n: int, graph: List[List[int]]) -> int: 
    def dfs(x: int, y: int) -> int: 
        if visited[x][y] != -1: 
            return visited[x][y]

        visited[x][y] = 1
        for i in range(4): 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and (graph[nx][ny] > graph[x][y]): 
                visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)

        return visited[x][y]

        ### ----- dfs() end ----- ###

    dx, dy = [-1,1,0,0], [0,0,1,-1]
    visited = [[-1] * n for _ in range(n)]

    for i in range(n): 
        for j in range(n): 
            if visited[i][j] == -1: 
                dfs(i, j)
    
    ans = 0
    for i in range(n): 
        ans = max(ans, max(visited[i]))

    return ans

    ### ----- joyGo() end ----- ###



if __name__ == "__main__": 
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    print(joyGo(n, graph))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, n, graph, ans"), 
    [
        (
            1, 
            4, [[14, 9, 12, 10], [1, 11, 5, 4], [7, 15, 2, 13], [6, 3, 16, 8]],
            4
        )
    ]
)

def test_joyGo(case_num: int, n: int, graph: List[List[int]], ans: int) -> None: 
    res = joyGo(n, graph)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ