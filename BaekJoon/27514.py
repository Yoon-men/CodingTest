# 백준27514 : 1차원 2048
def joyGo(total) : 
    tmp = 1
    while True : 
        num = 2**tmp
        if total < num : return 2**(tmp-1)
        tmp += 1

if __name__ == "__main__" : 
    _ = int(input())
    Li = list(map(int, input().split()))

    print(joyGo(sum(Li)))