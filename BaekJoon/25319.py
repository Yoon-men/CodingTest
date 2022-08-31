# 백준25319 : Twitch Plays VIIIbit Explorer
import sys
input = sys.stdin.readline

N, M, S = map(int, input().split())
items = [list(input().strip()) for _ in range(N)]
nickname = input().strip()

# Let's find 'C'        (Mission reward = C * 100,000,000 won)
nickname_appearNum = {i : 0 for i in set(nickname)}
for i in range(N) : 
    for j in range(M) : 
        if items[i][j] in nickname : 
            nickname_appearNum[items[i][j]] += 1
C = min(nickname_appearNum.values())

# Let's find the number of movements
obj = list(nickname) * 2
itemMap = [[1]*M for _ in range(N)]
y, x = 0, 0
route = []

while len(obj) > 0 : 
    if itemMap[y][x] == 1 : 
        if items[y][x] == obj[0] : 
            route.append("P")
            obj.pop(0)
            itemMap[y][x] = 0
    
    if obj[0] in items[y] : 
        if itemMap[y][items[y].index(obj[0])] == 1 : 
            route.append("")
        pass            # Test code / please delete the contents of this line.
    
    
        

print(C, len(route))
print(*route, sep="")