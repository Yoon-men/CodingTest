# 백준2161 : 카드1
from collections import deque
import sys
N = int(sys.stdin.readline())
cards = deque(range(1, N+1))
while len(cards) != 0 : 
    print(cards.popleft(), end=" ")
    if len(cards) != 0 : 
        cards.append(cards.popleft())