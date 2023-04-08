# 백준2501 : 약수 구하기
import sys; input = sys.stdin.readline

def joyGo(N: int, K: int) -> int : 
    Li = [i for i in range(1, N+1) if N%i == 0]
    if K > len(Li) : 
        return 0
    return Li[K-1]

if __name__ == "__main__" : 
    N, K = map(int, input().split())
    print(joyGo(N, K))