# 백준1213 : 팰린드롬 만들기
from collections import Counter

s = sorted(input())
odd = Counter(s)
oddCnt = 0
c = ""
for i in odd : 
    if odd[i] % 2 != 0 : 
        oddCnt += 1
        c = i
        s.remove(i)
    if oddCnt > 1 : break

if oddCnt > 1 : 
    print("I'm Sorry Hansoo")
else : 
    res = ""
    for i in range(0, len(s), 2) : 
        res += s[i]

    print(res + c + res[::-1])