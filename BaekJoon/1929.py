# 소수 구하기
import sys
input = sys.stdin.readline
M, N = map(int, input().split())

def primeCheck(num) : 
    if num == 1 : 
        return False
    else : 
        for i in range(2, int(num**0.5) + 1) : 
            if num % i == 0 : 
                return False
        return True

for i in range(M, N + 1) : 
    if primeCheck(i) : 
        print(i)