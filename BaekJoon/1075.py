# 백준1075 : 나누기
N = input()
F = int(input())

tmp = int(N[:-2]+"00")
while True : 
    if tmp % F == 0 : break
    tmp += 1

print(str(tmp)[-2:])