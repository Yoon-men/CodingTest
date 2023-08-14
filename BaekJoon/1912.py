# 백준1912 : 연속합
import sys; input = sys.stdin.readline
from typing import List

def joyGo(n: int, nums: List[int]) : 
    for i in range(1, n) : 
        nums[i] = max(nums[i], nums[i-1]+nums[i])
    
    return max(nums)


if __name__ == "__main__" : 
    n = int(input())
    nums = list(map(int, input().split()))

    print(joyGo(n, nums))