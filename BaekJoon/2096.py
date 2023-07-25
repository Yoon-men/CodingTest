# 백준2096 : 내려가기
import sys; input = sys.stdin.readline

N = int(input())
max_list = min_list = list(map(int, input().split()))

for _ in range(N-1) : 
    a, b, c = map(int, input().split())
    max_list = [a+max(max_list[0], max_list[1]), b+max(max_list), c+max(max_list[1], max_list[2])]
    min_list = [a+min(min_list[0], min_list[1]), b+min(min_list), c+min(min_list[1], min_list[2])]

print(max(max_list), min(min_list))