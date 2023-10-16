# 백준17388 : 와글와글 숭고한
Li = list(map(int, input().split()))
if sum(Li) >= 100 : print("OK")
else:
    if Li.index(min(Li)) == 0 : print("Soongsil")
    elif Li.index(min(Li)) == 1 : print("Korea")
    else : print("Hanyang")