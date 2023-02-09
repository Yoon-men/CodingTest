# 백준1292 : 쉽게 푸는 문제
A, B = map(int, input().split())
Li = []
for i in range(1, B+1) : 
    Li += [i for _ in range(i)]
print(sum(Li[A-1:B]))