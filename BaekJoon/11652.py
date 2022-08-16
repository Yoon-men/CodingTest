# 백준11652 : 카드
import sys
input = sys.stdin.readline
cards = {}
for _ in range(int(input())) : 
    card = int(input())
    if card in cards : 
        cards[card] += 1
    else : 
        cards[card] = 1
cards = dict(sorted(cards.items()))
print(max(cards, key=lambda x : cards[x]))