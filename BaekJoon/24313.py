# 백준24313 : 알고리즘 수업 - 점근적 표기 1
import sys; input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

print(1 if ((a1*n + a0 <= c*n) and (a1 <= c)) else 0)