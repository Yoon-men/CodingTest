# 백준2805 : 나무 자르기
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)


while start <= end : 
    mid = (start+end) // 2
    cut = 0
    for i in tree : 
        if i >= mid : 
            cut += i - mid
    if cut >= M : 
        start = mid + 1
    else : 
        end = mid - 1


print(end)