# 백준1818 : 책정리
import sys; input = sys.stdin.readline

def joyGo(N: int, Li: list) -> int : 
    dp = [0]
    for i in range(N) : 
        s, e = 0, len(dp)-1
        while s <= e : 
            m = (s+e) // 2
            if dp[m] < Li[i] : s = m + 1
            else : e = m - 1
        if s >= len(dp) : dp.append(Li[i])
        else : dp[s] = Li[i]

    return N - (len(dp)-1)


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))

    print(joyGo(N, Li))