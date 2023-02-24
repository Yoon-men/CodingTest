# 백준1978 : 소수 찾기
def isPrime(n) : 
    if n == 1 : return False

    for i in range(2, int(n**0.5)+1) : 
        if n % i == 0 : return False

    return True


if __name__ == "__main__" : 
    _ = int(input())
    Li = list(map(int, input().split()))

    ans = 0
    for i in Li : 
        if isPrime(i) : ans += 1

    print(ans)