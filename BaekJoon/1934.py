# 백준1934 : 최소공배수
import sys
input = sys.stdin.readline

for _ in range(int(input())) : 
    A, B = map(int, input().split())
    a, b = A, B
    while b != 0 : 
        a %= b
        a, b = b, a
    GCD = a             # Great Common Divisor(GCD)
    LCM = A*B // GCD    # Least Common Multiple(LCM)
    
    print(LCM)