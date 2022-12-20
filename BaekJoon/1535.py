# 백준1535 : 안녕
def chk(hp, dLi, hLi, N) : 
    dp = [[0]*(hp+1) for _ in range(N+1)]
    for i in range(1, N+1) : 
        for j in range(1, hp+1) : 
            if dLi[i-1] <= j : 
                dp[i][j] = max(hLi[i-1] + dp[i-1][j-dLi[i-1]], dp[i-1][j])
            else : 
                dp[i][j] = dp[i-1][j]
    return dp[N][hp-1]

if __name__ == "__main__" : 
    N = int(input())
    dLi = list(map(int, input().split()))     # demage list
    hLi = list(map(int, input().split()))     # happiness list
    hp = 100

    print(chk(hp, dLi, hLi, N))