# 백준25325 : 학생 인기도 측정
import sys; input = sys.stdin.readline

def joyGo(stu_data: dict, survey_list: list) -> list : 
    for survey in survey_list : 
        for stu in survey : 
            stu_data[stu] += 1
    
    return sorted(stu_data.items(), key=lambda x: -x[1])


if __name__ == "__main__" : 
    n = int(input())
    Di = {stu: 0 for stu in input().split()}
    Li = [input().split() for _ in range(n)]

    ans_list = joyGo(Di, Li)
    for key, val in ans_list : 
        print(key, val)