# 숫자 카드 2
from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
havingCards = input().split()
M = int(input())
check = input().split()
C = Counter(havingCards)
for card in check : 
    if card in C : 
        print(C[card], end=" ")
    else : 
        print(0, end=" ")