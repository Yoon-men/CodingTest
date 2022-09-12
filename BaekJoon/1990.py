# 백준1990 : 소수인팰린드롬
def isPalindrome(m) : 
    m = str(m)
    if m==m[::-1] : return True
    else : return False
def isPrime(m) : 
    if m==1 : return False
    for i in range(2, int(m**0.5)+1) : 
        if m%i==0 : return False
    return True

if __name__ == "__main__" : 
    a, b = map(int, input().split())
    if b>10000000 : b=10000000
    for i in range(a, b+1) : 
        if isPalindrome(i) : 
            if isPrime(i) : 
                print(i)
    print(-1)