# 백준1408 : 24
H1, M1, S1 = map(int, input().split(":"))
H2, M2, S2 = map(int, input().split(":"))

total = (H2*3600 + M2*60 + S2) - (H1*3600 + M1*60 + S1)
if total < 0 : total += 24*3600
H, M, S = total//3600, total%3600//60, total%60
print(f"{str(H).zfill(2)}:{str(M).zfill(2)}:{str(S).zfill(2)}")