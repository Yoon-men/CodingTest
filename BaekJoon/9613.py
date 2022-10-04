# 백준9613 : GCD 합
import sys ; input = sys.stdin.readline

def GCD(a, b) : 
    while b!=0 : c = a%b ; a = b ; b = c
    return a

if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        nums = list(map(int, input().split()))
        ans = 0
        for i in range(1, len(nums)) : 
            for j in range(i+1, len(nums)) : 
                ans += GCD(nums[i], nums[j])
        print(ans)