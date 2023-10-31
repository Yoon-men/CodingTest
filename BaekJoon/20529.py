# 백준20529 : 가장 가까운 세 사람의 심리적 거리
import sys; input = sys.stdin.readline
from typing import List

from itertools import combinations

def joyGo(N: int, mbtis: List[str]) -> int : 
    if N > 32 : return 0
    else : 
        ans = sys.maxsize
        for A, B, C in list(combinations(mbtis, 3)) : 
            tmp = 0
            for i in range(4) : 
                if A[i] != B[i] : tmp += 1
                if B[i] != C[i] : tmp += 1
                if C[i] != A[i] : tmp += 1
            ans = min(ans, tmp)

    return ans


if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        N = int(input())
        mbtis = input().split()

        print(joyGo(N, mbtis))