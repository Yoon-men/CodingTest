# 백준6219 : 소수의 자격
A, B, D = map(int, input().split())
Li = [1] * (B+1)
for i in range(2, int(B**0.5)+1) : 
    if Li[i] : 
        for j in range(i+i, B+1, i) : Li[j] = 0
prime_list = [i for i in range(A, B+1) if Li[i]]
ans = 0
for i in prime_list : 
    if str(D) in str(i) : ans += 1

print(ans)