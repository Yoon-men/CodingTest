# 최댓값

N = []

for _ in range(9) : 
    num = int(input(""))
    N.append(num)

print(max(N))
print(N.index(max(N)) + 1)