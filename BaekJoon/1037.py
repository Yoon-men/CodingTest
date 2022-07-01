# 백준1037 : 약수
import sys
input = sys.stdin.readline

N = int(input())
factor = list(map(int, input().split()))

A = max(factor)
B = min(factor)
print(A * B)