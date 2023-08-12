# 백준10798 : 세로읽기
import sys; input = sys.stdin.readline

def joyGo(board: list) -> list : 
    max_len = max(len(row) for row in board)
    ans = [board[j][i] for i in range(max_len) for j in range(5) if i < len(board[j])]

    return ans


if __name__ == "__main__" : 
    board = [input().strip() for _ in range(5)]
    print(*joyGo(board), sep='')