# 백준28701 : 세제곱의 합
N = int(input())
tmp = list(range(1, N+1))
print(sum(tmp))
print(sum(tmp)**2)
tmp_list = [i**3 for i in tmp]
print(sum(tmp_list))