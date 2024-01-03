# 백준19238 : 스타트 택시
import sys; input = sys.stdin.readline
from typing import List, Tuple
from collections import deque

def joyGo(N: int, M: int, fuel: int, graph: List[List[int]], start_x: int, start_y: int, driving_list: List[List[int]]) -> int: 
    def find_next_guy(_start_x: int, _start_y: int) -> Tuple[int, int, int]: 
        '''
        BFS를 사용해 가장 가까이 있는 다음 손님을 찾습니다.

        Parameters: 
            _start_x (int): 출발지의 x 좌표
            _start_y (int): 출발지의 y 좌표
        
        Returns: 
            Tuple[int, int, int]: 다음 손님을 찾을 수 있다면 손님의 출발지와 그 출발지까지의 거리를, 찾을 수 없다면 (-1, -1, -1)을 반환

        '''
        dq = deque([(_start_x, _start_y)])
        visited = [[-1] * N for _ in range(N)]
        visited[_start_x][_start_y] = 0

        guys = []

        while dq: 
            x, y = dq.popleft()
            if (x, y) in driving_dict.keys(): 
                guys.append((visited[x][y], x, y))
            if len(guys) == len(driving_dict): 
                break
            
            for i in range(4): 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < N) and (graph[nx][ny] != 1) and (visited[nx][ny] == -1): 
                    dq.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

        if not guys: 
            return (-1, -1, -1)
        
        return sorted(guys)[0]
    
        ### ----- find_next_guy() end ----- ###


    def getDistance(_start_x: int, _start_y: int, _end_x: int, _end_y: int) -> int: 
        '''
        BFS를 사용해 출발지와 목적지 사이의 거리를 구합니다.

        Parameters: 
            _start_x (int): 출발지의 x 좌표
            _start_y (int): 출발지의 y 좌표
            _end_x   (int): 목적지의 x 좌표
            _end_y   (int): 목적지의 y 좌표
        
        Returns: 
            int: 목적지에 도착할 수 있었다면 출발지부터 목적지까지의 거리, 도착할 수 없었다면 -1을 반환

        '''
        dq = deque([(_start_x, _start_y)])
        visited = [[-1] * N for _ in range(N)]
        visited[_start_x][_start_y] = 0

        while dq: 
            x, y = dq.popleft()
            if (x == _end_x) and (y == _end_y): 
                return visited[x][y]

            for i in range(4): 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < N) and (graph[nx][ny] != 1) and (visited[nx][ny] == -1): 
                    dq.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
        
        return -1
        
        ### ----- getDistance() end ----- ###


    start_x -= 1
    start_y -= 1

    dx, dy = [-1,1,0,0], [0,0,1,-1]

    driving_dict = {(row[0]-1, row[1]-1): (row[2]-1, row[3]-1) for row in driving_list}
    
    while driving_dict: 
        distance, start_x, start_y = find_next_guy(start_x, start_y)
        if (distance, start_x, start_y) == (-1, -1, -1): 
            return -1
        end_x, end_y = driving_dict[(start_x, start_y)]

        fuel -= distance

        distance = getDistance(start_x, start_y, end_x, end_y)
        if (distance > fuel) or (distance == -1): 
            return -1
        
        fuel += distance

        del driving_dict[(start_x, start_y)]
        start_x, start_y = end_x, end_y

    return fuel

    ### ----- joyGo() end ----- ###



if __name__ == "__main__": 
    N, M, fuel = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    start_x, start_y = map(int, input().split())
    driving_list = [list(map(int, input().split())) for _ in range(M)]

    print(joyGo(N, M, fuel, graph, start_x, start_y, driving_list))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, fuel, graph, start_x, start_y, driving_list, ans"), 
    [
        (
            1, 
            6, 3, 15,
            [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0]], 
            6, 5, 
            [[2, 2, 5, 6], [5, 4, 1, 6], [4, 2, 3, 5]], 
            14
        ), 
        (
            2, 
            6, 3, 13, 
            [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0]], 
            6, 5, 
            [[2, 2, 5, 6], [5, 4, 1, 6], [4, 2, 3, 5]], 
            -1
        ), 
        (
            3, 
            6, 3, 100, 
            [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0]], 
            6, 5, 
            [[2, 2, 5, 6], [5, 4, 1, 6], [4, 2, 3, 5]], 
            -1
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, fuel: int, graph: List[List[int]], start_x: int, start_y: int, driving_list: List[List[int]], ans: int) -> None: 
    res = joyGo(N, M, fuel, graph, start_x, start_y, driving_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ