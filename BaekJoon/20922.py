# 백준20922 : 겹치는 건 싫어
import sys; input = sys.stdin.readline
from collections import defaultdict

def joyGo(N: int, K: int, Li: list) -> int : 
    s, e = 0, 0
    cnt_dict = defaultdict(int)
    ans = 0

    while e < N : 
        a, b = Li[s], Li[e]
        if cnt_dict[b] < K : 
            cnt_dict[b] += 1
            e += 1
        else : 
            cnt_dict[a] -= 1
            s += 1
        ans = max(ans, e-s)

    return ans


if __name__ == "__main__" : 
    N, K = map(int, input().split())
    Li = list(map(int, input().split()))
    print(joyGo(N, K, Li))