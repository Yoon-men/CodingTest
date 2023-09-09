# 백준1507 : 궁금한 민호
import sys; input = sys.stdin.readline
from typing import Tuple

def joyGo(n: int, times: Tuple[Tuple[int]]) -> int : 
    graph = [[1]*(n) for _ in range(n)]
    for k in range(n) : 
        for i in range(n) : 
            for j in range(n) : 
                if (i == k) or (k == j) or (i == j) : continue
                if times[i][k] + times[k][j] == times[i][j] : 
                    graph[i][j] = 0
                elif times[i][k] + times[k][j] < times[i][j] : 
                    return -1
    
    answer = 0
    for i in range(n) : 
        for j in range(n) : 
            if graph[i][j] : answer += times[i][j]
    
    return answer // 2


if __name__ == "__main__" : 
    n = int(input())
    times = tuple(tuple(map(int, input().split())) for _ in range(n))
    print(joyGo(n, times))