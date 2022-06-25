# 백준25304 : 영수증
import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
priceSum = 0

for _ in range(N) : 
    price, num = map(int, input().split())
    priceSum += price * num

if X == priceSum : print("Yes")
else : print("No")