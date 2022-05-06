# 직각삼각형
import sys
input = sys.stdin.readline
while True : 
    lengths = list(map(int, input().split()))
    if lengths == [0, 0, 0] : 
        break
    lengths.sort()
    if lengths[0]**2 + lengths[1]**2 == lengths[2]**2 : 
        print("right")
    else : 
        print("wrong")