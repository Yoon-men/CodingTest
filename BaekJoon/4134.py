# 백준4134 : 다음 소수
import sys; input = sys.stdin.readline

def isPrime(n: int) -> bool : 
    if n <= 1 : return False
    for i in range(2, int(n**0.5)+1) : 
        if n%i == 0 : return False
    return True

if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        N = int(input())
        while True : 
            if isPrime(N) : print(N); break
            else : N += 1