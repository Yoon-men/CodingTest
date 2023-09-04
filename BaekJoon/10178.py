# 백준10178 : 할로윈의 사탕
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(Li: List[Tuple[int, int]]) -> None : 
    for a, b in Li : 
        print(f"You get {a//b} piece(s) and your dad gets {a%b} piece(s).")


if __name__ == "__main__" : 
    Li = [tuple(map(int, input().split())) for _ in range(int(input()))]
    joyGo(Li)