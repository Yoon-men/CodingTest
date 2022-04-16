# OX퀴즈
N = int(input())
for _ in range(N) : 
    score = 0
    bonusScore = 0
    answer = list(input())
    for marking in answer : 
        if marking == "O" : 
            bonusScore += 1
            score += bonusScore
        else : 
            bonusScore = 0
    print(score)