# 백준2239 : 스도쿠
import sys; input = sys.stdin.readline

def DFS(n: int) -> None : 
    if n == len(blank_list) : 
        for i in range(9) : 
            print(*board[i], sep='')
        sys.exit()
    
    x, y = blank_list[n]
    possible_list = [str(i) for i in range(1, 10)]
    # 가로 라인, 세로 라인 체크
    for i in range(9) : 
        if board[x][i] in possible_list : possible_list.remove(board[x][i])
        if board[i][y] in possible_list : possible_list.remove(board[i][y])
    
    # 3×3 박스 체크
    start_x, start_y = x//3 * 3, y//3 * 3
    for i in range(3) : 
        for j in range(3) : 
            already_num = board[start_x + i][start_y + j]
            if already_num in possible_list : possible_list.remove(already_num)
    
    for possible_num in possible_list : 
        board[x][y] = possible_num
        DFS(n+1)
        board[x][y] = 0


if __name__ == "__main__" : 
    board = [list(input().strip()) for _ in range(9)]
    blank_list = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '0']
    DFS(0)