# 백준3460 : 이진수
import sys; input = sys.stdin.readline
from typing import Tuple

def joyGo(nums: Tuple[int]) : 
    ans_list = []
    for num in nums : 
        binary_num = bin(num)[::-1]
        for i in range(len(binary_num)) : 
            if binary_num[i] == '1' : 
                ans_list.append(i)

    return ans_list


if __name__ == "__main__" : 
    nums = tuple(int(input()) for _ in range(int(input())))
    print(*joyGo(nums), sep=' ')