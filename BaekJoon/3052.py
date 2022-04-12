# 나머지
N = []
for _ in range(10) : 
    n = int(input())
    N.append(n)

for i in range(10) : 
    N[i] = N[i] % 42

differentNum = 0

if N[0] != N[1] : 
    differentNum += 1

N.sort()

for i in range(1, 10) : 
    if N[i] != N[i - 1] : 
        differentNum += 1

if differentNum == 0 : 
    differentNum = 1

print(differentNum)