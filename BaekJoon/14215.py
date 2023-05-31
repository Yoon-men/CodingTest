# 백준14215 : 세 막대
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> int : 
    Li.sort()
    return Li[0] + Li[1] + min(Li[2], Li[0]+Li[1]-1)


if __name__ == "__main__" : 
    Li = list(map(int, input().split()))

    print(joyGo(Li))