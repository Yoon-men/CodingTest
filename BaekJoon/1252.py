# 백준1252 : 이진수 덧셈
import sys; input = sys.stdin.readline

def joyGo(A: int, B: int) -> int : 
    A = int(A, 2)
    B = int(B, 2)
    
    return bin(A+B)[2:]


if __name__ == "__main__" : 
    A, B = input().split()
    print(joyGo(A, B))