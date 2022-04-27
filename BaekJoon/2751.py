# 수 정렬하기 2
import sys
input = sys.stdin.readline
N = int(input())
num = []
for _ in range(N) : 
    num.append(int(input()))
num.sort()
for i in num : 
    print(i)