# 백준11582 : 치킨 TOP N
import sys; input = sys.stdin.readline

def joyGo(N: int, Li: list, K: int) -> list : 
    ans_list = []

    for i in range(0, N, N//K) : 
        ans_list += sorted(Li[i:N//K+i])
    
    return ans_list


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))
    K = int(input())

    print(*joyGo(N, Li, K))