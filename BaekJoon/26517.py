# 백준26517 : 연속인가? ?
import sys; input = sys.stdin.readline

def joyGo(k: int, a: int, b: int, c: int, d: int) -> list : 
    A, B = a*k + b, c*k + d
    if A == B : return ["Yes", A]
    else : return ["No"]


if __name__ == "__main__" : 
    k = int(input())
    a, b, c, d = map(int, input().split())

    print(*joyGo(k, a, b, c, d))