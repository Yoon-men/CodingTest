# 백준2745 : 진법 변환
def joyGo(N: str, B: int) -> int : 
    return int(N, B)


if __name__ == "__main__" : 
    N, B = input().split()
    print(joyGo(N, int(B)))