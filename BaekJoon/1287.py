# 백준1287 : 할 수 있다
def chk(s) : 
    if s.find("()") >= 0 : return "ROCK"

    test = s.replace("+", "&").replace("-", "&").replace("/", "&").replace("*", "&")
    try : eval(test)
    except : return "ROCK"

    return eval(s.replace("/", "//"))

if __name__ == "__main__" : 
    print(chk(input()))