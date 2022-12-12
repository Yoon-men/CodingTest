# 백준15688 : 수 정렬하기 5
import sys ; input = sys.stdin.readline
Li = sorted([int(input()) for _ in range(int(input()))])
print("\n".join(str(i) for i in Li))