# 백준15726 : 이칙연산
A, B, C = map(int, input().split())
print(max(int(A*B/C), int(A/B*C)))