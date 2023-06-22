# 백준10797 : 10부제
N = int(input())
Li = list(map(int, input().split()))
cnt = 0
for i in Li : 
    if i == N : cnt += 1
print(cnt)