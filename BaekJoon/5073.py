# 백준5073 : 삼각형과 세 변
import sys; input = sys.stdin.readline
from typing import List

def joyGo(lens: List[int]) -> str : 
    lens.sort()
    return "Invalid" if (not lens[2] < sum(lens[:2])) else "Equilateral" if (len(set(lens)) == 1) else "Isosceles" if (len(set(lens)) == 2) else "Scalene"


if __name__ == "__main__" : 
    while True : 
        lens = list(map(int, input().split()))
        if lens[0] == 0 : break
        print(joyGo(lens))