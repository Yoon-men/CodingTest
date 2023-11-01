# 백준1149 : RGB거리
import sys; input = sys.stdin.readline
from typing import List

def joyGo(cost_list: List[List[int]]) -> int : 
    min_list = cost_list[0]
    for r, g, b in cost_list[1:] : 
        min_list = [min(min_list[1], min_list[2]) + r, min(min_list[0], min_list[2]) + g, min(min_list[0], min_list[1]) + b]
    
    return min(min_list)


if __name__ == "__main__" : 
    N = int(input())
    cost_list = [list(map(int, input().split())) for _ in range(N)]
    
    print(joyGo(cost_list))