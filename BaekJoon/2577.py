# 백준2577 : 숫자의 개수
import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

ABC = list(str(A * B * C))
for i in range(10) : 
    print(ABC.count(str(i)))