# 평균

N = int(input())
score = list(map(int, input().split()))

editedScore = []

for i in range(len(score)) : 
    editedScore.append(score[i] / max(score) * 100)

mean = sum(editedScore) / N
print(mean)