# 백준31090 : 2023은 무엇이 특별할까?
for _ in range(int(input())): 
    N = int(input())
    print("Good" if (N+1) % int(str(N)[-2:]) == 0 else "Bye")