# 백준2211 : 네트워크 복구
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, graph: List[List[Tuple[int, int]]]) -> List[Tuple[int, int]] : 
    parent_list = [0] * (N+1)

    distance_list = [sys.maxsize] * (N+1)
    distance_list[1] = 0

    hq = [(0, 1)]
    while hq : 
        current_distance, current_node = heappop(hq)
        if current_distance > distance_list[current_node] : continue

        for next_node, next_distance in graph[current_node] : 
            distance = current_distance + next_distance
            if distance < distance_list[next_node] : 
                parent_list[next_node] = current_node
                distance_list[next_node] = distance
                heappush(hq, (distance, next_node))
    
    return parent_list


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) : 
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
    
    parent_list = joyGo(N, graph)
    print(N-1)
    for i, j in enumerate(parent_list[2:], 2) : 
        print(i, j)

    # ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
#     N, M = 4, 5
#     tmp = '''1 2 1
# 1 4 4
# 1 3 2
# 4 2 2
# 4 3 3'''.split('\n')
#     graph = [[] for _ in range(N+1)]
#     for i in range(M) : 
#         A, B, C = map(int, tmp[i].split())
#         graph[A].append((B, C))
#         graph[B].append((A, C))
    
#     parent_list = joyGo(N, graph)
#     print(N-1)
#     for i, j in enumerate(parent_list[2:], 2) : 
#         print(i, j)
    # ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ