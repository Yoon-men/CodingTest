# 백준2628 : 종이자르기
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(W: int, H: int, Li: List[Tuple[int, int]]) : 
    row_list, col_list = [0, W], [0, H]
    
    for rc, val in Li : 
        if rc == 0 : col_list.append(val)
        else : row_list.append(val)
    
    row_list.sort()
    col_list.sort()

    w_list, h_list = [], []
    for i in range(len(row_list)-1) : 
        w_list.append(row_list[i+1] - row_list[i])
    for i in range(len(col_list)-1) : 
        h_list.append(col_list[i+1] - col_list[i])
    
    return max(w_list) * max(h_list)



if __name__ == "__main__" : 
    W, H = map(int, input().split())
    Li = [tuple(map(int, input().split())) for _ in range(int(input()))]

    print(joyGo(W, H, Li))