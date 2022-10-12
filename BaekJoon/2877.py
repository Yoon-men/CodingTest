# 백준2877 : 4와 7
K = int(input())
print(str(bin(K+1)[3:]).replace("0", "4").replace("1", "7"))