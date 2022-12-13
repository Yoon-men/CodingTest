# 백준11931 : 수 정렬하기 4
import sys ; input = sys.stdin.readline
Li = sorted([int(input()) for _ in range(int(input()))], reverse=True)
print("\n".join(str(i) for i in Li))