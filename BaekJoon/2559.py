# 백준2559 : 수열
import sys; input = sys.stdin.readline

def joyGo(N: int, K: int, Li: list) -> int : 
    sum_checker = ans = sum(Li[0:K])
    for i in range(1, N-K+1) : 
        sum_checker = sum_checker - Li[i-1] + Li[i+K-1]
        ans = max(ans, sum_checker)

    return ans


if __name__ == "__main__" : 
    N, K = map(int, input().split())
    Li = list(map(int, input().split()))

    print(joyGo(N, K, Li))