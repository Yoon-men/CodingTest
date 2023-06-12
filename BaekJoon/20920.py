# 백준20920 : 영단어 암기는 괴로워
import sys; input = sys.stdin.readline
from collections import defaultdict

def joyGo(N: int, M: int, Li: list) -> list : 
    Di = defaultdict(int)
    for word in Li : 
        if len(word) < M : continue
        Di[word] += 1
    
    tmp_list = sorted(Di.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    return [data[0] for data in tmp_list]


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = [input().strip() for _ in range(N)]

    print("\n".join(joyGo(N, M, Li)))