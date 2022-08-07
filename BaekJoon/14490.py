# 백준14490 : 백대열
def gcd(a, b) : 
    while b > 0 : 
        c = a % b
        a = b
        b = c
    return a

if __name__ == "__main__" : 
    n, m = map(int, input().split(":"))
    o = gcd(n, m)
    print(f"{n//o}:{m//o}")