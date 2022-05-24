# 숫자 카드
import sys
input = sys.stdin.readline
N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
checking = list(map(int, input().split()))

def finding(object, targetList, start, end) : 
    while start <= end : 
        mid = (start+end) // 2
        if targetList[mid] == object : 
            return True
        elif targetList[mid] > object : 
            end = mid - 1
        elif targetList[mid] < object : 
            start = mid + 1
    return False

for i in range(M) : 
    if finding(checking[i], cards, 0, N - 1) : 
        print(1, end = " ")
    else : 
        print(0, end = " ")