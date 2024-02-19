# 백준18398 : HOMWRK
import sys; input = sys.stdin.readline

for _ in range(int(input())): 
    for _ in range(int(input())): 
        A, B = map(int, input().split())
        print(f"{A+B} {A*B}")