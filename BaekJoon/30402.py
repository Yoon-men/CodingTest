# 백준30402 : 감마선을 맞은 컴퓨터
import sys; input = sys.stdin.readline
from typing import List

def joyGo(picture: List[List[str]]) -> str : 
    for row in picture : 
        row = set(row)
        if 'w' in row   : return "chunbae"
        elif 'b' in row : return "nabi"
        elif 'g' in row : return "yeongcheol"


if __name__ == "__main__" : 
    picture = [input().split() for _ in range(15)]
    
    print(joyGo(picture))