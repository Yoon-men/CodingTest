# 백준1182 : 부분수열의 합
import sys; input = sys.stdin.readline
from itertools import combinations

def joyGo(N: int, S: int, Li: list) -> int : 
    ans = 0

    for l in range(1, N+1) : 
        for c in combinations(Li, l) : 
            if sum(c) == S : ans += 1

    return ans


if __name__ == "__main__" : 
    N, S = map(int, input().split())
    Li = list(map(int, input().split()))

    print(joyGo(N, S, Li))