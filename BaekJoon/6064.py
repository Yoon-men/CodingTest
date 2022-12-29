# 백준6064 : 카잉 달력
import sys; input = sys.stdin.readline

def joyGo(M, N, x, y) : 
    ans = x
    while ans <= M*N : 
        if ((ans-x) % M == 0) and ((ans-y) % N == 0) : 
            return ans
        ans += M
    return -1

if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        M, N, x, y = map(int, input().split())
        print(joyGo(M, N, x, y))