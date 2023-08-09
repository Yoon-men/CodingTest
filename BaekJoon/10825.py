# 백준10825 : 국영수
import sys; input = sys.stdin.readline
Li = sorted([input().split() for _ in range(int(input()))], key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for stu in Li : 
    print(stu[0])