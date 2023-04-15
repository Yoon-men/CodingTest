# 백준9205 : 맥주 마시면서 걸어가기
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(n: int, home: tuple, convs: list, fest: tuple) -> None : 
    def BFS(start_point: tuple) -> None : 
        visited = [0] * n
        fx, fy = fest

        dq = deque([start_point])
        while dq : 
            x, y = dq.popleft()
            if abs(x-fx)+abs(y-fy) <= 1000 : 
                print("happy")
                return
            for i in range(n) : 
                if not visited[i] : 
                    cx, cy = convs[i]
                    if abs(x-cx)+abs(y-cy) <= 1000 : 
                        dq.append((cx, cy))
                        visited[i] = 1

        print("sad")

    BFS(home)


if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        n = int(input())
        home = tuple(map(int, input().split()))
        convs = [tuple(map(int, input().split())) for __ in range(n)]
        fest = tuple(map(int, input().split()))
        joyGo(n, home, convs, fest)