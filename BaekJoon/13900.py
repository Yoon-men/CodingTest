# 백준13900 : 순서쌍의 곱의 합
import sys; input = sys.stdin.readline

def joyGo(N: int, Li: list) -> int : 
    ans = 0
    sum_ = sum(Li)
    for num in Li : 
        sum_ -= num
        ans += num * sum_
    
    return ans


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))

    print(joyGo(N, Li))