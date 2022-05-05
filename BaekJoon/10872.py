# 팩토리얼
N = int(input())
def factorial(n) : 
    if n == 0 : 
        return 1
    elif n >= 1 : 
        return factorial(n-1) * n
print(factorial(N))