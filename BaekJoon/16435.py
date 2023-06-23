# 백준16435 : 스네이크버드
import sys; input = sys.stdin.readline

def joyGo(N: int, L: int, Li: list) -> int : 
    for height in sorted(Li) : 
        if L >= height : L += 1

    return L


if __name__ == "__main__" : 
    N, L = map(int, input().split())
    Li = list(map(int, input().split()))

    print(joyGo(N, L, Li))