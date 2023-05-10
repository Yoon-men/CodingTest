# 백준11000 : 강의실 배정
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def joyGo(N: int, Li: list) -> int : 
    Li = sorted(Li)

    queue = []
    heappush(queue, Li[0][1])

    for i in range(1, N) : 
        if Li[i][0] < queue[0] : 
            heappush(queue, Li[i][1])
        else : 
            heappop(queue)
            heappush(queue, Li[i][1])
    
    return len(queue)


if __name__ == "__main__" : 
    N = int(input())
    Li = [tuple(map(int, input().split())) for _ in range(N)]
    print(joyGo(N, Li))