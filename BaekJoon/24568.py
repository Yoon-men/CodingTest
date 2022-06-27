# 백준24568 : Cupcake Party
import sys
input = sys.stdin.readline


def party(R, S) : 
    CakeNum = R*8 + S*3
    answer = CakeNum - 28

    if answer < 0 : 
        answer = 0
    
    return answer


if __name__ == "__main__" : 
    R = int(input())            # Regular boxes (8 cupcakes per box)
    S = int(input())            # Small boxes   (3 cupcakes per box)
    print(party(R, S))