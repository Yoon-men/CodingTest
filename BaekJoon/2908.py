# 상수
A, B = list(map(str, input().split()))

A = list(A)
A[0], A[2] = A[2], A[0]

B = list(B)
B[0], B[2] = B[2], B[0]

realA = int("".join(A))
realB = int("".join(B))


if realA > realB : 
    print(realA)

else : 
    print(realB)