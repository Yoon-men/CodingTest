# 백준1010 : 다리 놓기
import sys ; input = sys.stdin.readline

def factorial(n) : 
    if n==0 : return 1
    elif n>=1 : return factorial(n-1) * n

if __name__ == "__main__" : 
    for i in range(int(input())) : 
        N, M = map(int, input().split())
        print(factorial(M)//(factorial(M-N)*factorial(N)))