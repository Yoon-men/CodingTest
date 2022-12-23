# 백준26594 : ZOAC 5
s = input()
ans = 0
for i in range(len(s)) : 
    ans += 1
    try : 
        if s[i] != s[i+1] : break
    except : 
        pass
print(ans)