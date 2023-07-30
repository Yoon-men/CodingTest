# 백준2566 : 최댓값
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> None : 
    _max = -1
    x, y = 0, 0
    for i in range(9) : 
        for j in range(9) : 
            if Li[i][j] > _max : 
                _max = Li[i][j]
                x, y = i+1, j+1
    
    print(_max)
    print(x, y)


if __name__ == "__main__" : 
    Li = [list(map(int, input().split())) for _ in range(9)]
    joyGo(Li)