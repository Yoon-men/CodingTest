# 백준11727 : 2×n 타일링 2
n = int(input())
Li = [1, 3]
for i in range(2, n) : 
    Li.append(Li[i-2]*2 + Li[i-1])
print(Li[n-1]%10007)