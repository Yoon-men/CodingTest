# 백준5032 : 탄산 음료
def joyGo(current: int, found: int, required: int) -> int : 
    current += found
    yeah = 0
    while current >= required : 
        yeah += current//required
        current = (current//required) + (current%required)
    return yeah

if __name__ == "__main__" : 
    e, f, c = map(int, input().split())
    print(joyGo(e, f, c))