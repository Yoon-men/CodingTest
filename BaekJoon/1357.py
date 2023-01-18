# 백준1357 : 뒤집힌 덧셈
X, Y = map(str, input().split())
X, Y = X[::-1], Y[::-1]
print(int(str(int(X)+int(Y))[::-1]))