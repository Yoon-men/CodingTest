# 백준7562 : 나이트의 이동
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(I: int, crt_x: int, crt_y: int, dest_x: int, dest_y: int) -> int: 
    dq = deque([(crt_x, crt_y)])
    adjacent = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

    visited = [[-1] * I for _ in range(I)]
    visited[crt_x][crt_y] = 0

    while dq: 
        x, y = dq.popleft()
        if (x == dest_x) and (y == dest_y): 
            return visited[x][y]
        
        for dx, dy in adjacent: 
            nx, ny = x+dx, y+dy
            if (0 <= nx < I) and (0 <= ny < I) and (visited[nx][ny] == -1): 
                dq.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1



if __name__ == "__main__": 
    for _ in range(int(input())): 
        I = int(input())
        crt_x, crt_y = map(int, input().split())
        dest_x, dest_y = map(int, input().split())

        print(joyGo(I, crt_x, crt_y, dest_x, dest_y))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, I, crt_x, crt_y, dest_x, dest_y, ans"), 
    [
        (
            1, 
            8, 
            0, 0, 
            7, 0, 
            5
        ), 
        (
            2, 
            100, 
            0, 0, 
            30, 50, 
            28
        ), 
        (
            3, 
            10, 
            1, 1, 
            1, 1, 
            0
        )
    ]
)

def test_joyGo(case_num: int, I: int, crt_x: int, crt_y: int, dest_x: int, dest_y: int, ans: int) -> None: 
    res = joyGo(I, crt_x, crt_y, dest_x, dest_y)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ