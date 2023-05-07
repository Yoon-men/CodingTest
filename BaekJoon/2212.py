# 백준2212 : 센서
import sys; input = sys.stdin.readline

def joyGo(N: int, K: int, Li: list) -> int : 
    Li = sorted(Li)
    distance_list = sorted([Li[i+1]-Li[i] for i in range(N-1)])
    return sum(distance_list[:N-K])

if __name__ == "__main__" : 
    N, K = int(input()), int(input())
    Li = list(map(int, input().split()))
    print(joyGo(N, K, Li))