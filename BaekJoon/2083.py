# 백준2083 : 럭비 클럽
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(members: List[Tuple[str, int, int]]) -> List[Tuple[str, str]] : 
    ans_list = [(name, "Senior" if ((age > 17) or (weight >= 80)) else "Junior") for name, age, weight in members]

    return ans_list


if __name__ == "__main__" : 
    members = []
    while True : 
        name, age, weight = input().split()
        if (name, age, weight) == ('#', '0', '0') : break
        members.append((name, int(age), int(weight)))
    
    for row in joyGo(members) : 
        print(*row)