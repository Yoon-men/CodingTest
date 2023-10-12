# 프로그래머스: 시소 짝꿍
from typing import List
from collections import defaultdict

def solution(weights: List[int]) -> int:
    answer = 0
    
    ratio_list = [1/1, 1/2, 2/1, 2/3, 3/2, 3/4, 4/3]
    weight_dict = defaultdict(int)
    
    for weight in weights : 
        for ratio in ratio_list : 
            answer += weight_dict[weight * ratio]
        weight_dict[weight] += 1

    return answer


if __name__ == "__main__" : 
    ## Test Case 1) ans: 4
    weights = [100,180,360,100,270]
    print(solution(weights))