# 백준5637 : 가장 긴 단어
import sys; input = sys.stdin.readline
from re import sub

def joyGo(txt_list: list) -> str : 
    txt_list = [sub("[^a-z-]", "", line) for line in txt_list]
    txt_list = sorted(txt_list, key=lambda x: len(x), reverse=True)

    return txt_list[0].lower()


if __name__ == "__main__" : 
    txt_list = []
    while True : 
        txt_list += input().split()
        if txt_list[-1] == "E-N-D" : break
    
    print(joyGo(txt_list))