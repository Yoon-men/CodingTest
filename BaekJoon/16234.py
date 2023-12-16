# 백준16234 : 인구 이동
import sys; input = sys.stdin.readline
from typing import List, Tuple
from collections import deque

def joyGo(N: int, L: int, R: int, board: List[List[int]]) -> int: 
    def bfs(start_x: int, start_y: int) -> List[Tuple[int, int]]: 
        dx, dy = [-1,1,0,0], [0,0,1,-1]

        dq = deque([(start_x, start_y)])
        visited[start_x][start_y] = 1

        union = [(start_x, start_y)]

        while dq: 
            x, y = dq.popleft()
            for i in range(4): 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]): 
                    if L <= abs(board[nx][ny] - board[x][y]) <= R: 
                        dq.append((nx, ny))
                        visited[nx][ny] = 1
                        union.append((nx, ny))
        
        return union

        ### ----- bfs() end ----- ###


    day = 0

    while True: 
        visited = [[0] * N for _ in range(N)]

        moving_flag = False

        for i in range(N): 
            for j in range(N): 
                if not visited[i][j]: 
                    union = bfs(i, j)
                    if len(union) > 1: 
                        moving_flag = True
                        num_of_people = sum([board[x][y] for x, y in union]) // len(union)
                        for x, y in union: 
                            board[x][y] = num_of_people

        day += 1

        if not moving_flag: return day-1

    ### ----- joyGo() end ----- ###



if __name__ == "__main__": 
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(joyGo(N, L, R, board))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, L, R, board, ans"), 
    [
        (1, 2, 20, 50, [[50, 30], [20, 40]], 1), 
        (2, 2, 40, 50, [[50, 30], [20, 40]], 0), 
        (3, 2, 20, 50, [[50, 30], [30, 40]], 1), 
        (4, 3, 5, 10, [[10, 15, 20], [20, 30, 25], [40, 22, 10]], 2), 
        (5, 4, 10, 50, [[10, 100, 20, 90], [80, 100, 60, 70], [70, 20, 30, 40], [50, 20, 100, 10]], 3)
    ]
)

def test_joyGo(case_num: int, N: int, L: int, R: int, board: List[List[int]], ans: int) -> None: 
    res = joyGo(N, L, R, board)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ