# 백준10867 : 중복 빼고 정렬하기
import sys; input = sys.stdin.readline
from typing import List

def joyGo(Li: List[int]) -> List[int] : 
    return sorted(set(Li))

if __name__ == "__main__" : 
    _ = input()
    Li = list(map(int, input().split()))
    print(*joyGo(Li))