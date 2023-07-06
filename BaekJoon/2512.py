# 백준2512 : 예산
import sys; input = sys.stdin.readline

def joyGo(Li: list, M: int) -> int : 
    if sum(Li) <= M : return max(Li)

    s, e = 0, max(Li)
    while s <= e : 
        m = (s+e) // 2

        total = 0
        for i in Li : 
            total += min(i, m)
        
        if total > M : e = m - 1
        else : s = m + 1

    return e


if __name__ == "__main__" : 
    _ = int(input())
    Li = list(map(int, input().split()))
    M = int(input())

    print(joyGo(Li, M))