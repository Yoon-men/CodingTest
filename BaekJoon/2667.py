# 백준2667 : 단지번호붙이기
import sys; input = sys.stdin.readline
from collections import deque       # For BFS

def joyGo(N: int, _map: list) -> None : 
    def BFS(x: int, y: int) -> int : 
        dq = deque([(x, y)])
        _map[x][y] = 0
        cnt = 1
        while dq : 
            x, y = dq.popleft()
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < N) and (_map[nx][ny]) : 
                    _map[nx][ny] = 0
                    cnt += 1
                    dq.append((nx, ny))

        return cnt


    def DFS(x: int, y: int, cnt: int) -> int : 
        _map[x][y] = 0
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (_map[nx][ny]) : 
                cnt = DFS(nx, ny, cnt+1)
        
        return cnt


    dx, dy = [-1,1,0,0], [0,0,1,-1]
    # ans_list = sorted([BFS(i, j) for i in range(N) for j in range(N) if _map[i][j]])        # For BFS
    ans_list = sorted([DFS(i, j, cnt=1) for i in range(N) for j in range(N) if _map[i][j]])         # For DFS

    print(len(ans_list))
    print(*ans_list, sep='\n')



if __name__ == "__main__" : 
    N = int(input())
    _map = [list(map(int, input().strip())) for _ in range(N)]

    joyGo(N, _map)

    # ㅠㅠㅠㅠㅠㅠ < Test code / please lock the contents of this line. > ㅠㅠㅠㅠㅠㅠ
#     N = 7
#     tmp = """0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000""".split('\n')
#     _map = [list(map(int, row)) for row in tmp]

#     joyGo(N, _map)
    # ㅛㅛㅛㅛㅛㅛ < Test code / please lock the contents of this line. > ㅛㅛㅛㅛㅛㅛ