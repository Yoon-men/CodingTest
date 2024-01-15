# 백준16948 : 데스 나이트
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(N: int, r1: int, c1: int, r2: int, c2: int) -> int: 
    dq = deque([(r1, c1, 0)])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    dx, dy = [-2,-2,0,0,2,2], [-1,1,-2,2,-1,1]

    while dq: 
        x, y, cnt = dq.popleft()
        if (x == r2) and (y == c2): 
            return cnt
        
        for i in range(6): 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]): 
                visited[nx][ny] = 1
                dq.append((nx, ny, cnt+1))
    
    return -1



if __name__ == "__main__": 
    N = int(input())
    r1, c1, r2, c2 = map(int, input().split())

    print(joyGo(N, r1, c1, r2, c2))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, r1, c1, r2, c2, ans"), 
    [
        (
            1, 
            7, 
            6, 6, 0, 1, 
            4
        ), 
        (
            2, 
            6, 
            5, 1, 0, 5, 
            -1
        ), 
        (
            3, 
            7, 
            0, 3, 4, 3, 
            2
        )
    ]
)

def test_joyGo(case_num: int, N: int, r1: int, c1: int, r2: int, c2: int, ans: int) -> None: 
    res = joyGo(N, r1, c1, r2, c2)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ