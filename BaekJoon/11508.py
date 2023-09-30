# 백준11508 : 2+1 세일
import sys; input = sys.stdin.readline
from typing import List

def joyGo(items: List[int]) -> int : 
    items.sort(reverse=True)
    ans = 0
    for i in range(len(items)) : 
        if i % 3 != 2 : ans += items[i]

    return ans


if __name__ == "__main__" : 
    items = [int(input()) for _ in range(int(input()))]
    print(joyGo(items))