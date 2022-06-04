# 백준5554 : 심부름 가는 길
import sys
input = sys.stdin.readline
A = int(input())
B = int(input())
C = int(input())
D = int(input())
time = A + B + C + D
print(time // 60)
print(time % 60)