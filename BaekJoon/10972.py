# 백준10972 : 다음 순열
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, Li: List[int]) -> List[int] : 
    for i in range(N-1, 0, -1) : 
        if Li[i-1] < Li[i] : 
            for j in range(N-1, 0, -1) : 
                if Li[i-1] < Li[j] : 
                    Li[i-1], Li[j] = Li[j], Li[i-1]
                    ans = Li[:i] + sorted(Li[i:])
                    return ans

    return [-1]


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))

    print(*joyGo(N, Li))