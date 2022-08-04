# 백준25375 : 아주 간단한 문제
import sys
input = sys.stdin.readline
for _ in range(int(input())) : 
    a, b = map(int, input().split())
    print(1 if a != b and b % a == 0 else 0)