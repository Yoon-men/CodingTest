# 백준19637 : IF문 좀 대신 써줘
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(titles: List[Tuple[str, str]], characters: List[int]) -> List[str] : 
    def binarySearch(character: int) -> str : 
        s, e = 0, len(titles)-1
        while s <= e : 
            m = (s+e) // 2
            if int(titles[m][1]) >= character : e = m-1
            else : s = m + 1
        
        return titles[e+1][0]


    ans_list = [binarySearch(character) for character in characters]

    return ans_list



if __name__ == "__main__" : 
    N, M = map(int, input().split())
    titles = [tuple(input().split()) for _ in range(N)]
    characters = [int(input()) for _ in range(M)]
    
    print(*joyGo(titles, characters), sep='\n')