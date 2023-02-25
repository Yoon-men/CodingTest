# 백준9237 : 이장님 초대
import sys; input = sys.stdin.readline
N = int(input())
Li = sorted(list(map(int, input().split())), reverse=True)
ansLi = [Li[i]+i+1 for i in range(N)]
print(max(ansLi) + 1)