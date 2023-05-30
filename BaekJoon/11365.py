# 백준11365 : !밀비 급일
import sys; input = sys.stdin.readline

while True : 
    txt = input().strip()
    if txt == "END" : break
    print(txt[::-1])