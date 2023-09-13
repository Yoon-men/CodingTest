# 백준2870 : 수학숙제
import sys; input = sys.stdin.readline
from typing import Tuple, List
from re import split as reSplit

def joyGo(txts: Tuple[str]) -> List[int] : 
    ans_list = []
    for txt in txts : ans_list += (reSplit("[a-z]", txt))
    
    ans_list = sorted([int(item) for item in ans_list if item])
    return ans_list


if __name__ == "__main__" : 
    txts = tuple(input().strip() for _ in range(int(input())))
    print(*joyGo(txts), sep='\n')
