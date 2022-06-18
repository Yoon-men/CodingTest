# 백준2775 : 부녀회장이 될테야
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) : 
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n+1)]

    for __ in range(k) : 
        for i in range(1, n) : 
            people[i] += people[i-1]

    print(people[n-1])