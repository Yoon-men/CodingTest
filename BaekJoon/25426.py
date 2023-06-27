# 백준25426 : 일차함수들
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> int : 
    N = len(Li)
    Li.sort()
    ans = 0
    for i in range(len(Li)) : 
        a, b = Li[i]
        ans += a*(i+1) + b
    
    return ans


if __name__ == "__main__" : 
    Li = [tuple(map(int, input().split())) for _ in range(int(input()))]

    print(joyGo(Li))