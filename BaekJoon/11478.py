# 백준11478 : 서로 다른 부분 문자열의 개수
import sys
input = sys.stdin.readline

S = input().strip()

answer = set()
for i in range(len(S)) : 
    for j in range(i, len(S)) : 
        divisionText = S[i:j+1]
        answer.add(divisionText)

print(len(answer))