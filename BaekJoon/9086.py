# 백준9086 : 문자열
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) : 
    text = input().strip()
    print(f"{text[0]}{text[-1]}")