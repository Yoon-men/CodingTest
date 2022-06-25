# 백준15727 : 조별과제를 하려는데 조장이 사라졌다
import sys
input = sys.stdin.readline

L = int(input())

if L % 5 == 0 : 
    print(L // 5)
else : 
    print(L//5 + 1)