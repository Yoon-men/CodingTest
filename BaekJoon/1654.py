# 백준1654 : 랜선 자르기
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
origin = [int(input()) for _ in range(K)]

minLength, maxLength = 1, max(origin)

while minLength <= maxLength : 
    midLength = (minLength+maxLength) // 2
    num = 0
    
    for line in origin : 
        num += line // midLength
    
    if num >= N : 
        minLength = midLength + 1
    else : 
        maxLength = midLength - 1

print(maxLength)