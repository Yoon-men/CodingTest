# 백준11948 : 과목선택
import sys; input = sys.stdin.readline
print(sum(sorted([int(input()) for _ in range(4)], reverse=True)[:3]) + max([int(input()) for _ in range(2)]))