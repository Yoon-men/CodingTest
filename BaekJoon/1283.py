# 백준1283 : 단축키 지정
import sys ; input = sys.stdin.readline

N = int(input())
Li = [input().strip() for _ in range(N)]

key = [" "]
ans = [0] * N

for i in range(N) : 
    tmp = Li[i].split()
    chk = 0
    for j in range(len(tmp)) : 
        if tmp[j][0].upper() not in key : 
            key.append(tmp[j][0].upper())
            tmp[j] = f"[{tmp[j][0]}]{tmp[j][1:]}"
            ans[i] = " ".join(tmp)
            chk = 1
            break

    if chk : continue
    for j in range(len(Li[i])) : 
        if Li[i][j].upper() not in key : 
            key.append(Li[i][j].upper())
            ans[i] = f"{Li[i][:j]}[{Li[i][j]}]{Li[i][j+1:]}"
            chk = 1
            break

    if chk : continue
    ans[i] = Li[i]

for i in ans : 
    print(i)