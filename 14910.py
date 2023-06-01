# 백준14910 : 오르막
Li = list(map(int, input().split()))
print("Good" if Li == sorted(Li) else "Bad")