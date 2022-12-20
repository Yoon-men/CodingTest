# 백준1535 : 안녕
N = int(input())
dLi = [0] + list(map(int, input().split()))     # demage list
hLi = [0] + list(map(int, input().split()))     # happiness list

hp = 100

dp = [[0]*(hp+1) for _ in range(N+1)]
for i in range(1, N+1) : 
    for j in range(1, hp+1) : 
        if dLi[i] <= j : 
            dp[i][j] = max(hLi[i-1] + dp[i-1][j-dLi[i]], dp[i-1][j])
        else : 
            dp[i][j] = dp[i-1][j]

print(dp[N][hp-1])