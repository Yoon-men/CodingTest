# 백준2607 : 비슷한 단어
import sys; input = sys.stdin.readline
from typing import Tuple

def joyGo(word_list: Tuple[str]) -> int : 
    first_word = word_list[0]
    ans = 0
    for word in word_list[1:] : 
        first = list(first_word)
        cnt = 0
        for c in word : 
            if c in first : first.remove(c)
            else          : cnt += 1
        if (cnt <= 1) and (len(first) <= 1) : ans += 1
    
    return ans


if __name__ == "__main__" : 
    word_list = tuple(input().strip() for _ in range(int(input())))
    print(joyGo(word_list))