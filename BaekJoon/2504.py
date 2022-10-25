# 백준2504 : 괄호의 값
s = input()
stack = []
ans = 0
tmp = 1

for i in range(len(s)) : 
    if s[i] == "(" : 
        stack.append(s[i])
        tmp *= 2
    elif s[i] == ")" : 
        if not stack or stack[-1] == "[" : ans = 0 ; break
        if s[i-1] == "(" : ans += tmp
        stack.pop()
        tmp //= 2
    elif s[i] == "[" : 
        stack.append(s[i])
        tmp *= 3
    elif s[i] == "]" : 
        if not stack or stack[-1] == "(" : ans = 0 ; break
        if s[i-1] == "[" : ans += tmp
        stack.pop()
        tmp //= 3

print(ans if not stack else 0)