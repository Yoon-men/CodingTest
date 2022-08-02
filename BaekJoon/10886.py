# 백준10886 : 0 = not cute / 1 = cute
import sys
input = sys.stdin.readline

Y = 0
N = 0
for _ in range(int(input())) : 
    if int(input()) == 1 : 
        Y += 1
    else : 
        N += 1

if Y > N : 
    print("Junhee is cute!")
else : 
    print("Junhee is not cute!")