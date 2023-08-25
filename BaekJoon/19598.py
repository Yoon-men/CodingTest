# 백준19598 : 최소 회의실 개수
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(times: List[Tuple[int, int]]) -> int : 
    times.sort()

    q = [times[0][1]]
    for i in range(1, len(times)) : 
        s, e = times[i]
        if s < q[0] : 
            heappush(q, e)
        else : 
            heappop(q)
            heappush(q, e)
    
    return len(q)


if __name__ == "__main__" : 
    times = [tuple(map(int, input().split())) for _ in range(int(input()))]
    print(joyGo(times))