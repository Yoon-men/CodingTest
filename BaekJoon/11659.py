# 백준11659 : 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sumLi = [0]

temp = 0
for i in nums : 
    temp += i
    sumLi.append(temp)

for _ in range(M) : 
    i, j = map(int, input().split())
    print(sumLi[j] - sumLi[i-1])