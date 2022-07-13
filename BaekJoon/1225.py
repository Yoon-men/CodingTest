# 백준1225 : 이상한 곱셈
import sys
A, B = map(str, sys.stdin.readline().split())
print(sum(map(int, A)) * sum(map(int, B)))