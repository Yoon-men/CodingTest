# 백준11653 : 소인수분해
import sys

N = int(sys.stdin.readline())

for num in range(2, N+1) : 
    if N % num == 0 : 
        while N % num == 0 : 
            print(num)
            N /= num