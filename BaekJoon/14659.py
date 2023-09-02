# 백준14659 : 한조서열정리하고옴ㅋㅋ
import sys; input = sys.stdin.readline
from typing import List

def joyGo(height: List[int]) : 
    ans = 0
    max_height = 0
    cnt = 0

    for h in height : 
        if h > max_height : 
            cnt = 0
            max_height = h
        else : 
            cnt += 1
        
        ans = max(cnt, ans)
    
    return ans


if __name__ == "__main__" : 
    _ = input()
    height = list(map(int, input().split()))

    print(joyGo(height))