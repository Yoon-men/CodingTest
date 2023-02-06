# 백준2702 : 초6 수학
import sys; input = sys.stdin.readline

def joyGo(A, B) : 
    a, b = A, B
    while b != 0 : 
        c = a % b
        a = b
        b = c
    GCD = a
    LCM = A*B // GCD

    return (LCM, GCD)


if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        a, b = map(int, input().split())
        print(*joyGo(a, b))