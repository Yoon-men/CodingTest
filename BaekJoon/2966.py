# 백준2966 : 찍기
N = int(input())
answers = list(input().strip())

sangeun = ['A', 'B', 'C']
changyeonog = ['B', 'A', 'B', 'C']
hyunjin = ['C', 'C', 'A', 'A', 'B', 'B']

score_dict = {"Adrian": 0, "Bruno": 0, "Goran": 0}

for i in range(N): 
    if answers[i] == sangeun[i % 3]: 
        score_dict["Adrian"] += 1
    if answers[i] == changyeonog[i % 4]: 
        score_dict["Bruno"] += 1
    if answers[i] == hyunjin[i % 6]: 
        score_dict["Goran"] += 1

max_score = max(score_dict.values())
print(max_score)
print('\n'.join([name for name, score in score_dict.items() if score == max_score]))