# 백준11053 : 가장 긴 증가하는 부분 수열
def joyGo() : 
    dp = [0] * N
    for i in range(N) : 
        for j in range(N) : 
            if (Li[i] > Li[j]) and (dp[i] < dp[j]) : 
                dp[i] = dp[j]
        dp[i] += 1

    return max(dp)


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))
    print(joyGo())