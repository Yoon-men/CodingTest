# 백준2583 : 영역 구하기
import sys; input = sys.stdin.readline
from typing import List, Tuple
from collections import deque

def joyGo(M: int, N: int, K: int, coordinates: List[Tuple[int, int, int, int]]) -> Tuple[int, List[int]]: 
    VISITABLE = 0
    WALL = 1
    VISITED = 2

    def getBoard() -> List[List[int]]: 
        board = [[VISITABLE] * N for _ in range(M)]

        for x1, y1, x2, y2 in coordinates: 
            for i in range(y1, y2): 
                for j in range(x1, x2): 
                    board[i][j] = WALL
        
        return board
    
        ### ----- getBoard() ----- ###
    

    def bfs(start_x: int, start_y: int) -> int: 
        dq = deque([(start_x, start_y)])
        dx, dy = (-1,1,0,0), (0,0,1,-1)

        cnt = 1
        board[start_x][start_y] = VISITED
        while dq: 
            x, y = dq.popleft()

            for i in range(4): 
                nx, ny = x+dx[i], y+dy[i]

                if (0 <= nx < M) and (0 <= ny < N) and (board[nx][ny] == VISITABLE): 
                    board[nx][ny] = VISITED
                    dq.append((nx, ny))
                    cnt += 1
        
        return cnt
    
        ### ----- bfs() ----- ###


    board = getBoard()

    blanks = []
    for i in range(M): 
        for j in range(N): 
            if board[i][j] == VISITABLE: 
                blanks.append(bfs(i, j))
    
    return (len(blanks), sorted(blanks))

    ### ----- joyGo() ----- ###



if __name__ == "__main__": 
    M, N, K = map(int, input().split())
    coordinates = [tuple(map(int, input().split())) for _ in range(K)]

    ans = joyGo(M, N, K, coordinates)
    print(ans[0])
    print(*ans[1])



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, M, N, K, coordinates, ans"), 
    [
        (
            1, 
            5, 7, 3, 
            [(0, 2, 4, 4), (1, 1, 2, 5), (4, 0, 6, 2)], 
            (3, [1, 7, 13])
        )
    ]
)

def test_joyGo(case_num: int, M: int, N: int, K: int, coordinates: List[Tuple[int, int, int, int]], ans: Tuple[int, List[int]]) -> None: 
    res = joyGo(M, N, K, coordinates)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ