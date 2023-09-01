# 백준2563 : 색종이
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(papers: List[Tuple[int, int]]) -> int : 
    board = [[0] * 100 for _ in range(100)]

    for x, y in papers : 
        for row in range(x, x+10) : 
            for col in range(y, y+10) : 
                board[row][col] = 1

    ans = 0
    for row in board : 
        ans += row.count(1)
    
    return ans


if __name__ == "__main__" : 
    papers = [tuple(map(int, input().split())) for _ in range(int(input()))]

    print(joyGo(papers))