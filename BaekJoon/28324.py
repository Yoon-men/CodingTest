# 백준28324 : 스케이트 연습
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, Li: List[int]) -> int : 
    v_list = [1] * N
    for i in range(N-2, -1, -1) : 
        v_list[i] = min(Li[i], v_list[i+1])
        if v_list[i]+1 <= Li[i] : v_list[i] += 1

    return sum(v_list)


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))

    print(joyGo(N, Li))