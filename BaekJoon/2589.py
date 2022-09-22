# 백준2589 : 보물섬
from collections import deque
import sys ; input = sys.stdin.readline

def joyGo(i, j) : 
    dq = deque()
    dq.append([i, j])
    visited = [[0]*H for _ in range(V)]
    visited[i][j] = 1
    cnt = 0
    while dq : 
        x, y = dq.popleft()
        for k in range(4) : 
            nx = x + dx[k]
            ny = y = dy[k]
            if (0 <= nx < H) and (0 <= ny < V) and (not visited[nx][ny]) and (m[nx][ny] == "L") : 
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                dq.append([nx, ny])
    print(visited)              # Test code / please delete the contents of this line.
    return cnt

if __name__ == "__main__" : 
    # V, H = map(int, input().split())              # Test code / please unlock the contents of this line.
    V, H = 5, 7             # Test code / please delete the contents of this line.
    # m = [input().strip() for _ in range(V)]               # Test code / please unlock the contents of this lien.
    m = "WLLWWWL LLLWLLL LWLWLWW LWLWLLL WLLWLWW".split()             # Test code / please delete the contents of this line.
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    answer = 0
    for i in range(V) : 
        for j in range(H) : 
            if m[i][j]=="L" : 
                answer = max(answer, joyGo(i, j))
    print(answer)