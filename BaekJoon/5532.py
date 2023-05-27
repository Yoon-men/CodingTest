# 백준5532 : 방학 숙제
import sys; input = sys.stdin.readline
from math import ceil

def joyGo(Li: list) -> int : 
    L, A, B, C, D = Li
    ans = L - max(ceil(A/C), ceil(B/D))

    return ans


if __name__ == "__main__" : 
    Li = [int(input()) for _ in range(5)]
    print(joyGo(Li))