# 백준 9944 : NxM 보드 완주하기
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, M: int, board: List[List[str]]) -> int: 
    def chk() -> bool: 
        for row in board: 
            if '.' in row: return False
        
        return True


    def DFS(x: int, y: int, cnt: int) -> None: 
        nonlocal ans
        if chk(): ans = min(ans, cnt)
        
        if ans > cnt: 
            for i in range(4): 
                nx, ny = x, y
                visited = []
                while True: 
                    nx, ny = nx+dx[i], ny+dy[i]
                    if (0 <= nx < N) and (0 <= ny < M) and (board[nx][ny] == '.'): 
                        visited.append((nx, ny))
                        board[nx][ny] = '*'
                    else: 
                        break

                if visited: DFS(visited[-1][0], visited[-1][1], cnt+1)
                
                for a, b in visited: board[a][b] = '.'
        
        return


    dx, dy = (-1,1,0,0), (0,0,1,-1)

    ans = sys.maxsize
    for i in range(N): 
        for j in range(M): 
            if board[i][j] == '*': continue

            board[i][j] = '*'
            DFS(i, j, 0)
            board[i][j] = '.'

    return -1 if (ans == sys.maxsize) else ans



if __name__ == "__main__": 
    case_num = 1
    while True: 
        try: 
            N, M = map(int, input().split())
            board = [list(input().strip()) for _ in range(N)]

            print(f"Case {case_num}: {joyGo(N, M, board)}")
            case_num += 1
        except: 
            break



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    "case_num, N, M, board, ans", 
    [
        (1, 5, 5, [['*', '*', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '*'], ['.', '.', '*', '.', '.'], ['.', '.', '.', '.', '.']], 10), 
        (2, 3, 4, [['*', '*', '*', '*'], ['*', '.', '.', '.'], ['*', '.', '.', '*']], 3)
    ]
)

def test_joyGo(case_num: int, N: int, M: int, board: List[List[str]], ans: int) -> None: 
    res = joyGo(N, M, board)
    assert res == ans, f"Test Case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ