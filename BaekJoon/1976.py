# 백준1976 : 여행 가자
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(N: int, board: List[List[int]], plan: List[int]) -> str: 
    def BFS(start: int) -> None: 
        dq = deque([start])
        while dq: 
            current = dq.popleft()
            visited[current] = 1

            for next in graph[current]: 
                if not visited[next]: 
                    visited[next] = 1
                    dq.append(next)
        
        return


    graph = [[] for _ in range(N)]
    for i in range(N): 
        for j in range(i, N): 
            if board[i][j]: 
                graph[i].append(j)
                graph[j].append(i)

    visited = [0] * N

    BFS(plan[0]-1)

    return "YES" if (all(visited[i-1] for i in plan)) else "NO"



if __name__ == "__main__": 
    N = int(input())
    M = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    plan = list(map(int, input().split()))

    print(joyGo(N, board, plan))


# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("N, board, plan, ans"), 
    [
        (3, [[0, 1, 0], [1, 0, 1], [0, 1, 0]], [1, 2, 3], "YES")
    ]
)

def test_joyGo(N: int, board: List[List[int]], plan: List[int], ans: str) -> None: 
    res = joyGo(N, board, plan)
    assert res == ans, f"Test Case 1 - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ