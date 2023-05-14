# 백준1264 : 모음의 개수
import sys; input = sys.stdin.readline

def joyGo(txt: str) -> int : 
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = 0
    for i in txt : 
        if i in vowel_list : ans += 1
    
    return ans


if __name__ == "__main__" : 
    while True : 
        txt = input().strip()
        if txt == '#' : break
        print(joyGo(txt))