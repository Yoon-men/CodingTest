# 백준5591 : 最大の和
import sys; input = sys.stdin.readline

def joyGo(n: int, k: int, Li: list) -> int : 
    sum_checker = ans = sum(Li[:k])
    for i in range(1, n-k+1) : 
        sum_checker = sum_checker - Li[i-1] + Li[i+k-1]
        ans = max(ans, sum_checker)
    
    return ans


if __name__ == "__main__" : 
    n, k = map(int, input().split())
    Li = [int(input()) for _ in range(n)]
    
    print(joyGo(n, k, Li))