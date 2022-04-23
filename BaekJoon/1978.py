# 소수 찾기
N = int(input())
figure = list(map(int, input().split()))
count = 0

for i in figure : 
    prime = True

    if i == 1 : 
        continue

    for j in range(2, i) : 
        if i % j == 0 : 
            prime = False
            break

    if prime == True : 
        count += 1

print(count)