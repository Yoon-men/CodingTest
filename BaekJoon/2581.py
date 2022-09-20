# 백준2581 : 소수
def isPrime(n) : 
    if n==1 : return False
    for i in range(2, int(n**0.5)+1) : 
        if n%i==0 : return False
    return True

if __name__ == "__main__" : 
    M = int(input())
    N = int(input())
    answer = []
    for i in range(M, N+1) : 
        if isPrime(i) : answer.append(i)
    print(f"{sum(answer)}\n{min(answer)}" if answer else -1)