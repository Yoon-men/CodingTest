# 백준10826 : 피보나치 수 4
n = int(input())
fLi = [0, 1]
for i in range(2, n+1) : 
    fLi.append(fLi[i-2] + fLi[i-1])
print(fLi[n])