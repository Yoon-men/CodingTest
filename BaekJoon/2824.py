# 백준2824 : 최대공약수
import sys ; input = sys.stdin.readline

def multiply(Li) : 
    result = 1
    for i in Li : result *= i
    return result
def joyGo(x, y) : 
    while y>0 : 
        z = x%y
        x = y
        y = z
    return x

if __name__ == "__main__" : 
    N = int(input())
    a = list(map(int, input().split()))
    A = multiply(a)
    M = int(input())
    b = list(map(int, input().split()))
    B = multiply(b)
    print(str(joyGo(A, B))[-9:])