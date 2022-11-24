# 백준1254 : 팰린드롬 만들기
s = input()
for i in range(len(s)) : 
    if s[i:] == s[i:][::-1] : 
        print(len(s) + i)
        break