# 곱셈
import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
def fuck(a, b) : 
    if b == 1 : 
        return a % C
    else : 
        wtf = fuck(a, b//2)
        if b%2 == 0 : 
            return (wtf*wtf) % C
        else : 
            return (wtf*wtf*a) % C
print(fuck(A, B))