# 백준24510 : 시간복잡도를 배운 도도
ans = 0
for _ in range(int(input())) : 
    s = input()
    ans = max(ans, s.count("for")+s.count("while"))
print(ans)