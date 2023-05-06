# 백준2003 : 수들의 합 2
import sys; input = sys.stdin.readline

def joyGo(N: int, M: int, Li: list) -> None : 
    s, e = 0, 0
    total = 0
    cnt = 0

    while True : 
        if total >= M : 
            if total == M : cnt += 1
            total -= Li[s]
            s += 1
        else : 
            if e == N : break
            total += Li[e]
            e += 1

    print(cnt)


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = list(map(int, input().split()))
    joyGo(N, M, Li)