# 백준2670 : 연속부분최대곱
import sys; input = sys.stdin.readline
from typing import List

def joyGo(nums: List[float]) -> float : 
    def round(N: float, ndigits: int = 1) -> float : 
        mul = 10 ** ndigits
        N *= mul
        N = int(N)+1 if (N-int(N) >= 0.5) else int(N)

        return N / mul


    for i in range(1, len(nums)) : 
        nums[i] = max(nums[i-1]*nums[i], nums[i])

    ans = max(nums)

    return f"{round(ans, 3):.3f}"



if __name__ == "__main__" : 
    nums = [float(input()) for _ in range(int(input()))]

    print(joyGo(nums))