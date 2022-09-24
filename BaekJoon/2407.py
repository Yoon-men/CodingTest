# 백준2407 : 조합
def factorial(N) : 
    if N == 0 : return 1
    elif N >= 1 : return factorial(N-1) * N 

if __name__ == "__main__" : 
    n, m = map(int, input().split())
    print(factorial(n)//(factorial(n-m)*factorial(m)))