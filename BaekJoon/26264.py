# 백준26264 : 빅데이터? 정보보호!
_ = input()
memo = input()
b, s = 0, 0
for i in memo : 
    if i == "b" : b += 1
    elif i == "s" : s += 1
print("bigdata?" if b > s else "bigdata? security!" if b == s else "security!")