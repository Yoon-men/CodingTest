# 수 찾기
import sys
input = sys.stdin.readline
N = int(input())
N_nums = list(map(int, input().split()))
N_nums.sort()
M = int(input())
M_nums = list(map(int, input().split()))
def detection(object) : 
    opening = 0
    ending = N - 1
    while opening <= ending : 
        mid = (opening+ending) // 2
        if N_nums[mid] == object : 
            return True
        elif object < N_nums[mid] : 
            ending = mid - 1
        elif object > N_nums[mid] :
            opening = mid + 1

for object in M_nums : 
    if detection(object) : 
        print(1)
    else : 
        print(0)