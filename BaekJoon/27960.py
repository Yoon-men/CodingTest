# 백준27960 : 사격 내기
A, B = map(int, input().split())
ans = 0
for i in range(9, -1, -1) : 
    score = 2**i
    a, b = 1 if A >= score else 0, 1 if B >= score else 0
    if a+b == 1 : 
        ans += score
        A -= score*(A >= score)
        B -= score*(B >= score)
    elif a+b == 2 : 
        A -= score
        B -= score
print(ans)