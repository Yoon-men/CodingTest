# 백준2670 : 연속부분최대곱
import sys; input = sys.stdin.readline
from typing import List

def joyGo(nums: List[float]) -> float : 
    for i in range(1, len(nums)) : 
        nums[i] = max(nums[i-1]*nums[i], nums[i])
    
    ans = max(nums)
    mul = 10**3
    ans *= mul
    ans = int(ans)+1 if (ans-int(ans) >= 0.5) else int(ans)

    return f"{ans / mul:.3f}"


if __name__ == "__main__" : 
    nums = [float(input()) for _ in range(int(input()))]

    print(joyGo(nums))