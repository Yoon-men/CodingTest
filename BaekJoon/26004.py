# 백준26004 : HI-ARC
from collections import defaultdict
N = int(input())
S = input()
di = defaultdict(int)
for i in S : 
    if i in "HIARC" : di[i] += 1
chk = 1
for i in "HIARC" : 
    if i not in di : 
        chk = 0
        break
print(min(di.values()) if chk else 0)