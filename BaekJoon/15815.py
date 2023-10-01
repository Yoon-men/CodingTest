# 백준15815 : 천재 수학자 성필
def joyGo(s: str) -> int : 
    stack = []
    for i in s : 
        if i.isdigit() : 
            stack.append(int(i))
        else : 
            b, a = stack.pop(), stack.pop()
            stack.append(a+b if i == '+' else a-b if i == '-' else a*b if i == '*' else a//b)
    
    return stack[0]


if __name__ == "__main__" : 
    print(joyGo(input()))