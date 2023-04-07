# 백준25631 : 마트료시카 합치기
from collections import Counter

def solve(N: int, Li: list) -> int : 
    cnt_dict = Counter(Li)
    return max(cnt_dict.values())


if __name__ == "__main__" : 
    N = int(input())
    Li = sorted(list(map(int, input().split())))

    print(solve(N, Li))