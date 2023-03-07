# 백준1417 : 국회의원 선거
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def joyGo(Li: list) -> int : 
    me = Li[0]

    que = []
    for num in Li[1:] : 
        heappush(que, (-num, num))

    ans = 0
    while que : 
        num = heappop(que)[1]
        if num >= me : 
            num -= 1
            me += 1
            ans += 1
            heappush(que, (-num, num))
    
    return ans


if __name__ == "__main__" : 
    N = int(input())
    Li = [int(input()) for _ in range(N)]

    print(joyGo(Li))