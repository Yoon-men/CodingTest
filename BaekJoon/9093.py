# 단어 뒤집기
T = int(input())
for _ in range(T) : 
    sentence = list(input().split())
    for i in sentence : 
        print(i[::-1], end = " ")