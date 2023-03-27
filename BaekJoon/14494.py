# 백준14494 : 다이나믹이 뭐예요?
def joyGo(n, m) : 
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1) : 
        for j in range(1, m+1) : 
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + dp[i-1][j]
    
    return dp[n][m]

if __name__ == "__main__" : 
    n, m = map(int, input().split())
    print(joyGo(n, m) % (10**9+7))