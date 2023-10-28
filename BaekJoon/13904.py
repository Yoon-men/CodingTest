# 백준13904 : 과제
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(assignment_list: List[Tuple[int, int]]) -> int : 
    queue = []
    deadline = -1
    for d, w in assignment_list : 
        heappush(queue, (-w, d))
        deadline = max(deadline, d)
    
    schedule_list = [0] * (deadline+1)
    while queue : 
        w, d = heappop(queue)
        
        for i in range(d, 0, -1) : 
            if schedule_list[i] : continue

            schedule_list[i] -= w
            break
    

    return sum(schedule_list)


if __name__ == "__main__" : 
    assignment_list = [tuple(map(int, input().split())) for _ in range(int(input()))]

    print(joyGo(assignment_list))