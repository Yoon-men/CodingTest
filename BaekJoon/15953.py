# 백준15953 : 상금 헌터
import sys
input = sys.stdin.readline

def first(n) : 
    if n == 0 : 
        return 0
    elif n == 1 : 
        return 5000000
    elif n <= 3 : 
        return 3000000
    elif n <= 6 : 
        return 2000000
    elif n <= 10 : 
        return 500000
    elif n <= 15 : 
        return 300000
    elif n <= 21 : 
        return 100000
    else : 
        return 0

def second(n) : 
    if n == 0 : 
        return 0
    elif n == 1 : 
        return 5120000
    elif n <= 3 : 
        return 2560000
    elif n <= 7 : 
        return 1280000
    elif n <= 15 : 
        return 640000
    elif n <= 31 : 
        return 320000
    else : 
        return 0

for _ in range(int(input())) : 
    a, b = map(int, input().split())
    print(first(a) + second(b))