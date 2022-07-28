# 백준12904 : A와 B
S = list(input())
T = list(input())

while len(S) != len(T) : 
    if T[-1] == "A" : 
        T.pop()
    elif T[-1] == "B" : 
        T.pop()
        T.reverse()

print(1 if S == T else 0)