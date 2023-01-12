# 백준25345 : 루나의 게임 세팅
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def factorial(n) : 
    if n == 0 : 
        return 1
    elif n >= 1 : 
        return factorial(n-1) * n

def nCr(n, r) : 
    return factorial(n) // (factorial(r) * factorial(n-r))

if __name__ == "__main__" : 
    N, K = map(int, input().split())
    _ = list(map(int, input().split()))

    print((nCr(N, K) * 2**(K-1)) % (10**9 + 7))