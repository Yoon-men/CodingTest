# 백준28074 : 모비스
s = set(input())
print("YES" if all(c in s for c in "MOBIS") else "NO")