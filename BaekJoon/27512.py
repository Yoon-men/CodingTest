# 백준27512 : 스네이크
n, m = map(int, input().split())
print(n*m if n*m % 2 == 0 else n*m-1)