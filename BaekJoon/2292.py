# 벌집
N = int(input())
check = 1
count = 1

while N > check : 
    check += 6 * count
    count += 1

print(count)