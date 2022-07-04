# 백준2953 : 나는 요리사다
import sys
scores = [sum(list(map(int, sys.stdin.readline().split()))) for _ in range(5)]
print(scores.index(max(scores))+1, max(scores))