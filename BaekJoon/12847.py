# 백준12847 : 꿀 아르바이트
import sys; input = sys.stdin.readline

def joyGo(n: int, m: int, Li: list) : 
    sum_checker = ans = sum(Li[:m])
    for i in range(1, n-m+1) : 
        sum_checker = sum_checker - Li[i-1] + Li[i+m-1]
        ans = max(ans, sum_checker)
    
    return ans


if __name__ == "__main__" : 
    n, m = map(int, input().split())
    Li = list(map(int, input().split()))

    print(joyGo(n, m, Li))