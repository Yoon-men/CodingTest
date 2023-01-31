# 백준14002 : 가장 긴 증가하는 부분 수열 4
def joyGo() : 
    dp = [0] * N
    for i in range(N) : 
        for j in range(N) : 
            if (Li[i] > Li[j]) and (dp[i] < dp[j]) : 
                dp[i] = dp[j]
        dp[i] += 1
    ans = max(dp)
    print(ans)

    pd, iL = dp[::-1], Li[::-1]
    ansLi = []
    for i in range(N) : 
        if pd[i] == ans :   
            ansLi.append(iL[i])
            ans -= 1
    print(*ansLi[::-1])


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))
    joyGo()