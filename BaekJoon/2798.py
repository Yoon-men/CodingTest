# 블랙잭
N, M = map(int, input().split())
cards = list(map(int, input().split()))
sum_of_card = []
for i in range(N) : 
    for j in range(i+1, N) : 
        for k in range(j+1, N) : 
            sum = cards[i] + cards[j] + cards[k]
            if sum > M : 
                pass
            else : 
                sum_of_card.append(sum)
print(max(sum_of_card))