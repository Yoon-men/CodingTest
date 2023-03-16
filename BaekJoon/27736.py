# 백준27736 : 찬반투표
N = int(input())
Li = list(map(int, input().split()))
A, R, I = Li.count(1), Li.count(-1), Li.count(0)
print("INVALID" if I >= N/2 else "APPROVED" if A > R else "REJECTED")