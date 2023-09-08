# 백준2503 : 숫자 야구
import sys; input = sys.stdin.readline
from typing import Tuple
from itertools import permutations

def joyGo(data: Tuple[Tuple[int, int, int]]) : 
    nums_list = list(permutations(range(1, 10), 3))
    removed_nums = set()

    for hyuk, strike, ball in data :    
        hyuk = tuple(map(int, str(hyuk)))
        
        for num in nums_list : 
            if num in removed_nums : continue 

            s = b = 0
            for idx in range(3) : 
                if hyuk[idx] == num[idx] : s += 1
                elif hyuk[idx] in num : b += 1
            
            if (s != strike) or (b != ball) : 
                removed_nums.add(num)

    return len(set(nums_list)-removed_nums)


if __name__ == "__main__" : 
    data = tuple(tuple(map(int, input().split())) for _ in range(int(input())))
    print(joyGo(data))