# 백준1343 : 폴리오미노
from typing import Union

def joyGo(s: str) -> Union[str, int] : 
    s = s.replace("XXXX", "AAAA")
    s = s.replace("XX", "BB")

    return -1 if ('X' in s) else s


if __name__ == "__main__" : 
    print(joyGo(input()))