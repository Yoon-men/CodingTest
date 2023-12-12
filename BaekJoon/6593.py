# 백준6593 : 상범 빌딩
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(L: int, R: int, C: int, building: List[List[List[str]]]) -> str: 
    def bfs(start_x: int, start_y: int, start_z: int): 
        dx, dy, dz = [0,0,0,0,1,-1], [-1,1,0,0,0,0], [0,0,1,-1,0,0]
        visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
        visited[start_x][start_y][start_z] = 1

        dq = deque([(start_x, start_y, start_z)])
        while dq: 
            x, y, z = dq.popleft()
            for i in range(6): 
                nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
                if (0 <= nx < L) and (0 <= ny < R) and (0 <= nz < C): 
                    if building[nx][ny][nz] == 'E': 
                        return f"Escaped in {visited[x][y][z]} minute(s)."
                    
                    if (building[nx][ny][nz] == '.') and (not visited[nx][ny][nz]): 
                        visited[nx][ny][nz] = visited[x][y][z] + 1
                        dq.append((nx, ny, nz))
                    
        return "Trapped!"


    for i in range(L): 
        for j in range(R): 
            for k in range(C): 
                if building[i][j][k] == "S": 
                    return bfs(i, j, k)



if __name__ == "__main__": 
    while True: 
        L, R, C = map(int, input().split())
        if L+R+C == 0: break

        building = [[] for _ in range(L)]
        for i in range(L): 
            building[i] = [list(input().strip()) for _ in range(R)]
            input()

        print(joyGo(L, R, C, building))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, L, R, C, building, ans"), 
    [
        (1, 3, 4, 5, [[['S', '.', '.', '.', '.'], ['.', '#', '#', '#', '.'], ['.', '#', '#', '.', '.'], ['#', '#', '#', '.', '#']], [['#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#'], ['#', '#', '.', '#', '#'], ['#', '#', '.', '.', '.']], [['#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#'], ['#', '.', '#', '#', '#'], ['#', '#', '#', '#', 'E']]], "Escaped in 11 minute(s)."), 
        (2, 1, 3, 3, [[['S', '#', '#'], ['#', 'E', '#'], ['#', '#', '#'], []]], "Trapped!")
    ]
)

def test_joyGo(case_num: int, L: int, R: int, C: int, building: List[List[List[str]]], ans: str) -> None: 
    res = joyGo(L, R, C, building)
    assert res == ans, f"Test Case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ