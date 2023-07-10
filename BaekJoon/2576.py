# 백준2576 : 홀수
import sys; input = sys.stdin.readline
Li = [int(input()) for _ in range(7)]
Li = sorted([i for i in Li if i % 2 == 1])
print('\n'.join(map(str, (sum(Li), Li[0]))) if Li else -1)