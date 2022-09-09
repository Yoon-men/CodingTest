# 백준1747 : 소수&팰린드롬
def joyGo(n) : 
    def isPalindrome(m) : 
        m = str(m)
        if m==m[::-1] : return True
        else : return False
    def isPrime(m) : 
        if m==1 : return False
        for i in range(2, m) : 
            if m%i==0 : return False
        return True

    while True : 
        if isPalindrome(n) : 
            if isPrime(n) : 
                return n
        n += 1

if __name__ == "__main__" : 
    print(joyGo(int(input())))