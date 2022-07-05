# 백준10807 : 개수 세기
import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
v = int(input())
print(nums.count(v))