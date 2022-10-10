# 백준25711 : 인경산
import sys ; input = sys.stdin.readline

N, Q = map(int, input().split())
X_Li = list(map(int, input().split()))
Y_Li = list(map(int, input().split()))

f_Li = [0] * N
b_Li = [0] * N
for i in range(N-1) : 
    if Y_Li[i] < Y_Li[i+1] : f_Li[i+1] = f_Li[i] + ((Y_Li[i+1]-Y_Li[i])**2 + (X_Li[i+1]-X_Li[i])**2)**0.5 * 3
    elif Y_Li[i] == Y_Li[i+1] : f_Li[i+1] = f_Li[i] + (X_Li[i+1]-X_Li[i]) * 2
    elif Y_Li[i] > Y_Li[i+1] : f_Li[i+1] = f_Li[i] + ((Y_Li[i]-Y_Li[i+1])**2 + (X_Li[i+1]-X_Li[i])**2)**0.5
for i in range(1, N) : 
    if Y_Li[i] < Y_Li[i-1] : b_Li[i] = b_Li[i-1] + ((Y_Li[i-1]-Y_Li[i])**2 + (X_Li[i]-X_Li[i-1])**2)**0.5 * 3
    elif Y_Li[i] == Y_Li[i-1] : b_Li[i] = b_Li[i-1] + (X_Li[i]-X_Li[i-1]) * 2
    elif Y_Li[i] > Y_Li[i-1] : b_Li[i] = b_Li[i-1] + ((Y_Li[i]-Y_Li[i-1])**2 + (X_Li[i]-X_Li[i-1])**2)**0.5

for _ in range(Q) : 
    departure, arrival = map(int, input().split())
    ans = 0
    if departure < arrival : print(f_Li[arrival-1] - f_Li[departure-1])
    else : print(b_Li[departure-1] - b_Li[arrival-1])