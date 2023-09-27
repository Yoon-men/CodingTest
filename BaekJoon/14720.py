# 백준14720 : 우유 축제
import sys; input = sys.stdin.readline
from typing import List

def joyGo(stores: List[int]) : 
    step, ans = 0, 0
    for store in stores : 
        if step == store : 
            step = (step+1) % 3
            ans += 1
    
    return ans


if __name__ == "__main__" : 
    _ = input()
    stores = list(map(int, input().split()))
    print(joyGo(stores))