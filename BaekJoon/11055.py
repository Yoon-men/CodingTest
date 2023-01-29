# 백준11055 : 가장 큰 증가 부분 수열
def joyGo() : 
    dp = Li[:]
    for i in range(N) : 
        for j in range(i) : 
            if Li[i] > Li[j] :      # 현재 idx의 숫자가 앞에 있는 숫자보다 클 경우
                dp[i] = max(dp[i], Li[i]+dp[j])

    return max(dp)


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))
    print(joyGo())