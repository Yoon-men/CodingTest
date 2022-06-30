# 백준2869 : 달팽이는 올라가고 싶다
import sys
A, B, V = map(int, sys.stdin.readline().split())
answer = (V-B)/(A-B)
print(int(answer) if answer == int(answer) else int(answer)+1)