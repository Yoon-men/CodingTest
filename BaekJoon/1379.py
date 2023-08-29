# 백준1379 : 강의실 2
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, classes: List[Tuple[int, int, int]]) -> List[int] : 
    ans_list = [0] * (N+1)
    classes.sort(key=lambda x: (x[1], x[2]))

    ans_list[0] = 1
    ans_list[classes[0][0]] = ans_list[0]
    q = [(classes[0][2], classes[0][0])]
    for i in range(1, N) : 
        n, s, e = classes[i]
        if s < q[0][0] : 
            ans_list[0] += 1
            ans_list[n] = ans_list[0]
            heappush(q, (e, n))
        else : 
            ans_list[n] = ans_list[q[0][1]]
            heappop(q)
            heappush(q, (e, n))

    return ans_list


if __name__ == "__main__" : 
    N = int(input())
    classes = [tuple(map(int, input().split())) for _ in range(N)]

    print(*joyGo(N, classes), sep='\n')