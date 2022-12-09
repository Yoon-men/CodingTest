# 백준1251 : 단어 나누기
word = list(input())
ansLi = []

for i in range(1, len(word)-1) : 
    for j in range(i+1, len(word)) : 
        first = word[:i]
        second = word[i:j]
        third = word[j:] 

        ansLi.append("".join(first[::-1]+second[::-1]+third[::-1]))

print(min(ansLi))