# 백준17427 : 약수의 합 2
import sys; input = sys.stdin.readline

def joyGo(N) : 
    ans = 0
    for i in range(1, N+1) : 
        ans += (N//i) * i
    
    return ans


if __name__ == "__main__" : 
    N = int(input())
    print(joyGo(N))