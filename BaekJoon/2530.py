# 인공지능 시계
import sys
A, B, C = map(int, sys.stdin.readline().split())
D = int(sys.stdin.readline())

C += D
B += C//60
A += B//60
print(A % 24, B % 60, C % 60)