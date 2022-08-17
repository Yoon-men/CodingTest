# 백준15624 : 피보나치 수 7
n = int(input())
fLi = [0, 1]
for i in range(2, n+1) : 
    fLi.append(fLi[i-2]%1000000007 + fLi[i-1]%1000000007)
print(fLi[n] % 1000000007)