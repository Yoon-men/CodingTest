# 백준2747 : 피보나치 수
def joyGo(n) : 
    dp = [0, 1]
    for i in range(2, n+1) : 
        dp.append(dp[i-2] + dp[i-1])
    return dp[-1]

if __name__ == "__main__" : 
    print(joyGo(int(input())))