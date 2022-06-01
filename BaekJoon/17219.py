# 백준17219 : 비밀번호 찾기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = {}

for _ in range(N) : 
    address, pw = map(str, input().split())
    data[address] = pw

for _ in range(M) : 
    print(data[input().strip()])