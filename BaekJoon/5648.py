# 백준5648 : 역원소 정렬
import sys; input = sys.stdin.read

def joyGo(N: str, Li: list) -> list : 
    return sorted([int(num[::-1]) for num in Li])

if __name__ == "__main__" : 
    N, *Li = input().split()
    print("\n".join(map(str, joyGo(N, Li))))