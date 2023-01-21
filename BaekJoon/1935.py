# 백준1935 : 후위 표기식2
import sys; input = sys.stdin.readline

N = int(input())
equation = input().strip()
Li = [int(input()) for _ in range(N)]

s = []
for i in equation : 
    if i.isalpha() : 
        s.append(Li[ord(i)-ord("A")])
    else : 
        b, a = s.pop(), s.pop()
        if   i == "+" : s.append(a + b)
        elif i == "-" : s.append(a - b)
        elif i == "*" : s.append(a * b)
        elif i == "/" : s.append(a / b)

print(f"{s[0]:.2f}")