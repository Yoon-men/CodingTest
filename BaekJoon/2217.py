# 백준2217 : 로프
import sys; input = sys.stdin.readline

def joyGo(N: int, Li: list) -> int : 
    Li.sort(reverse=True)
    ans_list = [Li[i]*(i+1) for i in range(N)]

    return max(ans_list)


if __name__ == "__main__" : 
    N = int(input())
    Li = [int(input()) for _ in range(N)]

    print(joyGo(N, Li))