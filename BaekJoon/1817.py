# 백준1817 : 짐 챙기는 숌
import sys; input = sys.stdin.readline

def joyGo(N: int, M: int, Li: list) -> int : 
    if not N : return 0
    
    cnt, ans = 0, 1
    for i in Li : 
        if cnt + i > M : 
            ans += 1
            cnt = i
        else : 
            cnt += i
    
    return ans


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = list(map(int, input().split()))

    print(joyGo(N, M, Li))