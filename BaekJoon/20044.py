# 백준 20044 : Project Teams
import sys; input = sys.stdin.readline
from typing import List

def joyGo(n: int, capacity_list: List[int]) -> int : 
    capacity_list.sort()
    ans = sys.maxsize
    for i in range(n) : 
        ans = min(ans, capacity_list[i] + capacity_list[2*n-i-1])
    
    return ans


if __name__ == "__main__" : 
    n = int(input())
    capacity_list = list(map(int, input().split()))
    print(joyGo(n, capacity_list))