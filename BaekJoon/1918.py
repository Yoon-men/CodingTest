# 백준1918 : 후위 표기식
def joyGo(s: str) -> str : 
    ans = ''
    stack = []
    for i in s : 
        if i.isalpha() : ans += i
        elif i == '(' : stack.append(i)
        elif (i == '+') or (i == '-') : 
            while stack and (stack[-1] != '(') : ans += stack.pop()
            stack.append(i)
        elif (i == '*') or (i == '/') : 
            while stack and ((stack[-1] == '*') or (stack[-1] == '/')) : ans += stack.pop()
            stack.append(i)
        elif i == ')' : 
            while stack and (stack[-1] != '(') : ans += stack.pop()
            stack.pop()
    
    while stack : ans += stack.pop()
    
    return ans


if __name__ == "__main__" : 
    print(joyGo(input()))