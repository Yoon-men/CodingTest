# 백준4299 : AFC 윔블던
S, M = map(int, input().split())
if S < M : print(-1)
else : 
    a, b = (S+M)//2, (S-M)//2
    if (a+b == S) and (a-b == M) : print(a, b)
    else : print(-1)