# 백준11728 : 배열 합치기
_, _ = map(int, input().split())
print(*sorted(list(map(int, input().split())) + list(map(int, input().split()))))