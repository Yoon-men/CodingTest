# 백준27433 : 팩토리얼 2
def joyGo(N: int) -> int : 
    def factorial(n: int) -> int : 
        if n == 0 : return 1
        else : return factorial(n-1) * n
    
    return factorial(N)


if __name__ == "__main__" : 
    print(joyGo(int(input())))