# 백준 27434 : 팩토리얼 3
import sys
sys.setrecursionlimit(10**9)

def joyGo(N: int) -> None : 
    def factorial(n: int) -> int : 
        if n == 0 : 
            return 1
        elif n > 0 : 
            return factorial(n-1) * n
    
    print(factorial(N))


if __name__ == "__main__" : 
    joyGo(int(input()))