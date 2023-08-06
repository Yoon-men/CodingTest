# 백준5568 : 카드 놓기
import sys; input = sys.stdin.readline
from itertools import permutations

def joyGo(k: int, Li: list) -> int : 
    Se = set()
    for perm in list(permutations(Li, k)) : 
        Se.add(''.join(perm))
    
    return len(Se)


if __name__ == "__main__" : 
    n = int(input())
    k = int(input())
    Li = [input().strip() for _ in range(n)]

    print(joyGo(k, Li))