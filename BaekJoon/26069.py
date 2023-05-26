# 백준26069 : 붙임성 좋은 총총이
from collections import defaultdict
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> int : 
    Di = defaultdict(bool)
    Di["ChongChong"] = True
    ans = 1
    for A, B in Li : 
        if Di[A] : 
            if not Di[B] : 
                Di[B] = True
                ans += 1
        elif Di[B] : 
            if not Di[A] : 
                Di[A] = True
                ans += 1

    return ans


if __name__ == "__main__" : 
    Li = [input().split() for _ in range(int(input()))]
    print(joyGo(Li))