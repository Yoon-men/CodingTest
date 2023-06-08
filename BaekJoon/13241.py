# 백준 13241 : 최소공배수
def joyGo(A: int, B: int) -> int : 
    a, b = A, B
    while b != 0 : 
        c = a % b
        a, b = b, c
    GCD = a
    LCM = A*B // GCD

    return LCM


if __name__ == "__main__" : 
    A, B = map(int, input().split())
    print(joyGo(A, B))