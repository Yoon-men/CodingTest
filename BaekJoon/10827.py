# 백준10827 : a^b
a, b = input().split() ; b = int(b)
c = len(a.split(".")[1]) * b
d = str(int(a.replace(".", "")) ** b)
if a.split(".")[0] != "0" : 
    print(f"{d[:len(d)-c]}.{d[len(d)-c:]}")
else : 
    print(f"0.{'0'*(c-len(d))}{d}")