# 백준13565 : 침투
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(M: int, N: int, material: List[List[str]]) -> str: 
    def bfs(start_x: int, start_y: int): 
        dq = deque([(start_x, start_y)])
        dx, dy = (-1,1,0,0), (0,0,1,-1)

        visited = [[0] * N for _ in range(M)]

        while dq: 
            x, y = dq.popleft()

            if x == M-1: 
                return True
            
            for i in range(4): 
                nx, ny = x+dx[i], y+dy[i]
                
                if (0 <= nx < M) and (0 <= ny < N) and (not visited[nx][ny]): 
                    if material[nx][ny] == '0': 
                        dq.append((nx, ny))
                        visited[nx][ny] = 1
        
        return False
    
        ### ----- bfs() ----- ###


    for i in range(N): 
        if (material[0][i] == '0') and (bfs(0, i) == True): 
            return "YES"
    
    return "NO"

    ### ----- joyGo() ----- ###



if __name__ == "__main__": 
    M, N = map(int, input().split())
    material = [list(input().strip()) for _ in range(M)]

    print(joyGo(M, N, material))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, M, N, material, ans"), 
    [
        (
            1, 
            5, 6, 
            [['0', '1', '0', '1', '0', '1'], ['0', '1', '0', '0', '0', '0'], ['0', '1', '1', '1', '0', '1'], ['1', '0', '0', '0', '1', '1'], ['0', '0', '1', '0', '1', '1']], 
            "NO"
        ), 
        (
            2, 
            8, 8, 
            [['1', '1', '0', '0', '0', '1', '1', '1'], ['0', '1', '1', '0', '0', '0', '0', '0'], ['0', '0', '0', '1', '1', '0', '0', '1'], ['1', '1', '0', '0', '1', '0', '0', '0'], ['1', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '1', '1', '1', '1', '0', '0'], ['0', '1', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '0', '1', '0', '1', '1']], 
            "YES"
        )
    ]
)

def test_joyGo(case_num: int, M: int, N: int, material: List[List[str]], ans: str) -> None: 
    res = joyGo(M, N, material)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ