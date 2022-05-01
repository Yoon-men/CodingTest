# 오븐 시계
H, M = map(int, input().split())
required = int(input())
M += required
if M >= 60 : 
    H += M//60
    M %= 60
if H >= 24 : 
    H -= 24
print(f"{H} {M}")