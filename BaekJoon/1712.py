# 백준1712 : 손익분기점
def joyGo(A: int, B: int, C: int) -> int : 
    if B >= C : return -1
    else : return int(A/(C-B)+1)


if __name__ == "__main__" : 
    A, B, C = map(int, input().split())
    print(joyGo(A, B, C))