# 백준25644 : 최대 상승
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> int : 
    yeah, ans = 0, 0
    for price in Li[::-1] : 
        yeah = max(yeah, price)
        ans = max(ans, yeah-price)
    
    return ans


if __name__ == "__main__" : 
    _ = int(input())
    Li = list(map(int, input().split()))

    print(joyGo(Li))