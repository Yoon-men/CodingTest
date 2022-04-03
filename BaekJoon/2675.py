# 문자열 반복

T = int(input(""))                      # 테스트 케이스의 개수
P = []                                  # 문자열

for _ in range(T) : 
    R, S = list(map(str, input().split()))     
    S = list(S)
    result = ""

    for i in range(len(S)) : 
        result += S[i] * int(R)
    
    P.append(result)

for i in range(len(P)) : 
    print(P[i])