# 백준25628 : 햄버거 만들기
A, B = map(int, input().split())
answer = 0
for _ in range(B) : 
    if A >= 2 : answer += 1 ; A-=2
    else : break
print(answer)