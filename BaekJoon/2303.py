# 백준2303 : 숫자 게임
import sys; input = sys.stdin.readline
from typing import List
from itertools import combinations

def joyGo(N: int, player_list: List[List[int]]) -> int : 
    result_list = [0] * N
    for i in range(N) : 
        _max = 0
        for able in list(combinations(player_list[i], 3)) : 
            _max = max(_max, sum(able)%10)
        result_list[i] = _max
    
    ans = 1
    _max = result_list[0]
    for i in range(1, N) : 
        if result_list[i] >= _max : 
            ans = i+1
            _max = result_list[i]

    return ans


if __name__ == "__main__" : 
    N = int(input())
    player_list = [list(map(int, input().split())) for _ in range(N)]
    print(joyGo(N, player_list))