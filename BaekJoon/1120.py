# 백준1120 : 문자열
A, B = input().split()
Li = []
for i in range(len(B) - len(A) + 1) : 
    cnt = 0
    for j in range(len(A)) : 
        if A[j] != B[i+j] : cnt += 1
    Li.append(cnt)
print(min(Li))