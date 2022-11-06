# 백준25915 : 연세여 사랑한다
s = ord(input())
Di = {chr(i) : i for i in range(65, 91)}
ans = 0
for i in list("ILOVEYONSEI") : 
    ans += abs(s-ord(i))
    s = ord(i)
print(ans)