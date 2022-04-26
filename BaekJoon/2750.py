# 수 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
numList = []

for _ in range(N) : 
    num = int(input())
    numList.append(num)

numList.sort()

for i in range(N) : 
    print(numList[i])