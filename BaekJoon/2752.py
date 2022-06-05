# 백준2752 : 세수정렬
import sys
nums = sorted(list(map(int, sys.stdin.readline().split())))
print(" ".join(str(i) for i in nums))