# 백준1106 : 호텔
import sys ; input = sys.stdin.readline

def chk(C, cLi) : 
    dp = [0] + [sys.maxsize for _ in range(C+100)]
    for cost, customer in cLi : 
        for i in range(customer, C+100) : 
            dp[i] = min(dp[i-customer]+cost, dp[i])
    return min(dp[C:])

if __name__ == "__main__" : 
    C, N = map(int, input().split())
    cLi = [0] * N       # cost & customer list
    for i in range(N) : 
        cLi[i] = list(map(int, input().split()))
    print(chk(C, cLi))