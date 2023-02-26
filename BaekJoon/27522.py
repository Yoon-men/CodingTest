# 백준27522 : 카트라이더: 드리프트
import sys; input = sys.stdin.readline
Li = [None] * 8
for i in range(8) : 
    R, T = map(str, input().split())
    M, S, s = map(int, R.split(":"))
    Li[i] = ((M, S, s), T)

scoreLi = [10, 8, 6, 5, 4, 3, 2, 1]
R, B = 0, 0
for ranking, data in enumerate(sorted(Li)) : 
    if data[1] == "R" : R += scoreLi[ranking]
    else : B += scoreLi[ranking]

if R == B : print("Red" if Li[0][1] == "R" else "Blue")
else : print("Red" if R > B else "Blue")