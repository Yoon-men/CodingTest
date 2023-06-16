# 백준11899 : 괄호 끼워넣기
def joyGo(S: str) -> int : 
    s = []
    for i in S : 
        if i == '(' : 
            s.append(i)
        else : 
            if s and (s[-1] == '(') : s.pop()
            else : s.append(i)

    return len(s)


if __name__ == "__main__" : 
    print(joyGo(input()))