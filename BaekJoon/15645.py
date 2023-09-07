# 백준15645 : 내려가기 2
import sys; input = sys.stdin.readline
from typing import Tuple

def joyGo(board: Tuple[Tuple[int, int, int]]) : 
    max_list = min_list = board[0]
    for a, b, c in board[1:] : 
        max_list = [max(max_list[0], max_list[1]) + a, max(max_list[0], max_list[1], max_list[2]) + b, max(max_list[1], max_list[2]) + c]
        min_list = [min(min_list[0], min_list[1]) + a, min(min_list[0], min_list[1], min_list[2]) + b, min(min_list[1], min_list[2]) + c]

    return f"{max(max_list)} {min(min_list)}"


if __name__ == "__main__" : 
    board = tuple(tuple(map(int, input().split())) for _ in range(int(input())))

    print(joyGo(board))