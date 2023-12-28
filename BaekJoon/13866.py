# 백준13866 : 팀 나누기
import sys; input = sys.stdin.readline

A, B, C, D = map(int, input().split())
print(abs((A + D) - (B + C)))