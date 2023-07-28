# 백준3040 : 백설 공주와 일곱 난쟁이
import sys; input = sys.stdin.readline
from itertools import combinations

def joyGo(Li: list) -> tuple : 
    comb_list = list(combinations(Li, 7))

    for comb in comb_list : 
        if sum(comb) == 100 : 
            return comb


if __name__ == "__main__" : 
    Li = [int(input()) for _ in range(9)]
    print(*joyGo(Li), sep='\n')