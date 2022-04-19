# 알파벳 찾기
sentence = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet : 
    if i in sentence : 
        print(sentence.index(i), end = " ")
    else : 
        print(-1, end = " ")