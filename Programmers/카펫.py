# 프로그래머스: 카펫
from typing import Tuple

def solution(brown: int, yellow: int) -> Tuple[int, int] : 
    for yello_width in range(1, yellow+1) : 
        if yellow % yello_width != 0 : continue

        yello_height = yellow // yello_width
        w, h = 2+yello_width, yello_height+2
        brown_num = (2 * yello_height) + w * 2
        if (brown_num == brown) and (w >= h) : return (w, h)


if __name__ == "__main__" : 
    ## Test Case 1) ans: [4, 3]
    print(solution(10, 2))

    ## Test Case 2) ans: [3, 3]
    print(solution(8, 1))

    ## Test Case 3) ans: [8, 6]
    print(solution(24, 24))