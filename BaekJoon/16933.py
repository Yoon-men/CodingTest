# 백준16933 : 벽 부수고 이동하기 3
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(N: int, M: int, K: int, graph: List[List[str]]) -> int: 
    TURN = 1

    dx, dy = [-1,1,0,0], [0,0,1,-1]
    visited: List[List[List[int]]] = [[[sys.maxsize] * (K+1) for _ in range(M)] for _ in range(N)]
    dq = deque([(0, 0, K, TURN)])
    
    while dq: 
        x, y, z, turn = dq.popleft()
        if (x == N-1) and (y == M-1): return turn
        
        for i in range(4): 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < M): 
                if (graph[nx][ny] == '1') and (z > 0) and (visited[nx][ny][z-1] > turn): 
                    if turn % 2 == 1: 
                        dq.append((nx, ny, z-1, turn+1))
                        visited[nx][ny][z-1] = turn
                    else: 
                        dq.append((x, y, z, turn+1))
                elif (graph[nx][ny] == '0') and (visited[nx][ny][z] > turn): 
                    dq.append((nx, ny, z, turn+1))
                    visited[nx][ny][z] = turn
    
    return -1

    ### ----- joyGo() end ----- ###



if __name__ == "__main__": 
    N, M, K = map(int, input().split())
    graph = [list(input().strip()) for _ in range(N)]

    print(joyGo(N, M, K, graph))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, K, graph, ans"), 
    [
        (1, 1, 4, 1, [['0', '0', '1', '0']], 5), 
        (2, 1, 4, 1, [['0', '1', '0', '0']], 4), 
        (3, 6, 4, 1, [['0', '1', '0', '0'], ['1', '1', '1', '0'], ['1', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '1', '1', '1'], ['0', '0', '0', '0']], 15), 
        (4, 6, 4, 2, [['0', '1', '0', '0'], ['1', '1', '1', '0'], ['1', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '1', '1', '1'], ['0', '0', '0', '0']], 9), 
        (5, 1, 1, 1, [['0']], 1), 
        (6, 3, 3, 2, [['0', '1', '1'], ['1', '1', '1'], ['1', '1', '0']], -1), 
        (7, 2, 4, 2, [['0', '1', '1', '1'], ['0', '1', '1', '0']], 7), 
        (8, 3, 3, 10, [['0', '1', '1'], ['0', '1', '1'], ['0', '0', '0']], 5), 
        (9, 3, 3, 3, [['0', '1', '1'], ['1', '1', '1'], ['1', '1', '0']], 7), 
        (10, 5, 5, 4, [['0', '1', '1', '0', '1'], ['1', '1', '1', '0', '0'], ['0', '0', '1', '1', '1'], ['1', '1', '1', '1', '0'], ['0', '0', '1', '1', '0'], []], 10)
    ]
)

def test_joyGo(case_num: int, N: int, M: int, K: int, graph: List[List[str]], ans: int) -> None: 
    res = joyGo(N, M, K, graph)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ