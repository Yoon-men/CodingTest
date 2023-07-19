# 백준11966 : 2의 제곱인가?
Li = [2**i for i in range(31)]
print(1 if int(input()) in Li else 0)