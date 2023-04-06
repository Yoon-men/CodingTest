# 백준10162 : 전자레인지
T = int(input())

if T % 10 == 0 : 
    A, B, C = T//300, (T%300)//60, ((T%300)%60)//10
    print(A, B, C)
else : 
    print(-1)