# 백준10974 : 모든 순열
import sys; input = sys.stdin.readline
from itertools import permutations

def joyGo(N: int) -> None : 
    for per in list(permutations(range(1, N+1), N)) : 
        print(*per)


if __name__ == "__main__" : 
    joyGo(int(input()))