# 좌표 압축
import sys
input = sys.stdin.readline
_ = int(input())
dots = list(map(int, input().split()))
RE_dots = sorted(list(set(dots)))
ZIP_dots = {RE_dots[i] : i for i in range(len(RE_dots))}
print(" ".join(str(ZIP_dots[i]) for i in dots))