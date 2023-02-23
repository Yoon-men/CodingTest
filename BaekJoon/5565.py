# 백준5565 : 영수증
import sys; input = sys.stdin.readline
print(int(input())-sum([int(input()) for _ in range(9)]))