# 검증수
N = list(map(int, input().split()))
num = 0
for i in N : 
    num += i**2
print(num % 10)