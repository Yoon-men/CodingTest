# 백준4158 : CD
import sys; input = sys.stdin.readline
from typing import List

def joyGo(geun: List[int], yeong: List[int]) -> int : 
    ans = 0
    geun = set(geun)
    for cd in yeong : 
        if cd in geun : ans += 1

    return ans


if __name__ == "__main__" : 
    while True : 
        N, M = map(int, input().split())
        if (N == 0) and (M == 0) : break

        geun = [int(input()) for _ in range(N)]
        yeong = [int(input()) for _ in range(M)]

        print(joyGo(geun, yeong))