# 백준4766 : 일반 화학 실험
import sys; input = sys.stdin.readline

a = float(input())
while True : 
    b = float(input())
    if b == 999 : break
    print(f"{b-a:.2f}")
    a = b