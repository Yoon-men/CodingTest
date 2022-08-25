# 백준11726 : 2×n 타일링
n = int(input())
Li = [1, 2]
for i in range(2, n) : 
    Li.append(Li[i-2] + Li[i-1])
print(Li[n-1]%10007)