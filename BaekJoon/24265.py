# 백준24265 : 알고리즘 수업 - 알고리즘의 수행 시간 4
def joyGo(n: int) -> list : 
    return [sum([i for i in range(n)]), 2]

if __name__ == "__main__" : 
    print("\n".join(map(str, joyGo(int(input())))))