# 백준27919 : UDPC 파티
def joyGo(V: str) -> str : 
    UC, DP = 0, 0
    for vote in V : 
        if (vote == "U") or (vote == "C") : UC += 1
        elif (vote == "D") or (vote == "P") : DP += 1
    
    ans = ""
    if UC > (DP+1)//2 : ans += "U"
    if DP > 0 : ans += "DP"

    return ans


if __name__ == "__main__" : 
    V = input()
    print(joyGo(V))