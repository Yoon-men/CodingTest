# 백준13022 : 늑대와 올바른 단어
from collections import defaultdict

def chk(s) : 
    wolf = defaultdict(int)
    Li = ["w", "o", "l", "f"]; numChk = 0
    for idx in range(len(s)) : 
        wolf[s[idx]] += 1
        try :       # indexError 우회용
            if s[idx] != "w" : 
                if wolf[s[idx]] != wolf["w"] : 
                    if s[idx] != s[idx+1] : return 0        # 카운트 틀림
                if s[idx+1] == "w" : wolf = defaultdict(int)
            if s[idx] != s[idx+1] : 
                numChk += 1
            if Li[numChk%4] != s[idx+1] : return 0          # 순서 틀림
        except : pass
    if (len(wolf) < 4) or (len(set(wolf.values())) > 1): return 0
    return 1

if __name__ == "__main__" : 
    print(chk(input()))