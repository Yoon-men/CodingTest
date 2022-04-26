# 제로
K = int(input())
ledger = []
for _ in range(K) : 
    num = int(input())
    if num == 0 : 
        ledger.pop()
    else : 
        ledger.append(num)
print(sum(ledger))