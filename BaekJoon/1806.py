# 백준1806 : 부분합
import sys; input = sys.stdin.readline

def joyGo(N: int, S: int, Li: list) -> None : 
    s, e = 0, 0
    total = 0
    ans = sys.maxsize

    while True : 
        if total >= S : 
            ans = min(ans, e-s)
            total -= Li[s]
            s += 1
        else : 
            if e == N : break
            total += Li[e]
            e += 1

    print(0 if ans == sys.maxsize else ans)


if __name__ == "__main__" : 
    N, S = map(int, input().split())
    Li = list(map(int, input().split()))
    joyGo(N, S, Li)