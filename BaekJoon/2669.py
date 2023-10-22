# 백준2669 : 직사각형 네개의 합집합의 면적 구하기
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(squares: List[Tuple[int, int, int, int]]) : 
    board = [[0 for _ in range(100)] for _ in range(100)]

    for x1, y1, x2, y2 in squares : 
        for i in range(x1, x2) :
            for j in range(y1, y2) : board[i][j] = 1
    
    ans = 0
    for row in board : ans += sum(row)

    return ans


if __name__ == "__main__" : 
    squares = [tuple(map(int, input().split())) for _ in range(4)]
    print(joyGo(squares))