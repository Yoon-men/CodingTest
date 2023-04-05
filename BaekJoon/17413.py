# 백준17413 : 단어 뒤집기 2
def joyGo(s: str) -> str : 
    s = list(s)
    idx = 0
    while idx < len(s) : 
        if s[idx] == "<" : 
            idx += 1
            while s[idx] != ">" : idx += 1
            idx += 1
        elif (s[idx].isalpha()) or (s[idx].isdigit()) : 
            startIdx = idx
            while (idx < len(s)) and ((s[idx].isalpha()) or (s[idx].isdigit())) : idx += 1
            tmpString = s[startIdx:idx][::-1]
            s[startIdx:idx] = tmpString
        else : 
            idx += 1

    return "".join(s)


if __name__ == "__main__" : 
    print(joyGo(input()))