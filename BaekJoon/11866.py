# 요세푸스 문제 0
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
nums = list(range(1, N+1))
permutation = []
i = K-1

for _ in range(N) : 
    while True : 
        if i >= len(nums) : 
            i -= len(nums)
        else : 
            break
    permutation.append(nums[i])
    del nums[i]
    i += K-1

print("<", end = "")
for i in range(len(permutation)) : 
    if i != len(permutation)-1 : 
        print(permutation[i], end = ", ")
    else : 
        print(permutation[i], end = "")
print(">", end = "")