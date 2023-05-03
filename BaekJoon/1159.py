# 백준1159 : 농구 경기
import sys; input = sys.stdin.readline
from collections import defaultdict

def joyGo(name_list: list) -> None : 
    name_dict = defaultdict(int)
    for name in name_list : 
        name_dict[name[0]] += 1

    ans_list = []
    for name, num in sorted(name_dict.items()) : 
        if num >= 5 : ans_list.append(name)

    print("".join(ans_list) if ans_list else "PREDAJA")
    

if __name__ == "__main__" : 
    name_list = [input().strip() for _ in range(int(input()))]
    joyGo(name_list)