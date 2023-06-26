# 백준2910 : 빈도 정렬
import sys; input = sys.stdin.readline
from collections import defaultdict

def joyGo(N: int, C: int, Li: list) -> list : 
    Di = defaultdict(int)
    for item in Li : 
        Di[item] += 1
    
    tmp = sorted(Di.items(), key=lambda x: x[1], reverse=True)
    ans_list = [item for item, cnt in tmp for _ in range(cnt)]

    return ans_list


if __name__ == "__main__" : 
    N, C = map(int, input().split())
    Li = list(map(int, input().split()))

    print(*joyGo(N, C, Li))