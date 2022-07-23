# 백준1541 : 잃어버린 괄호
equation = input().split("-")
for i in range(len(equation)) : 
    equation[i] = sum(map(int, equation[i].split("+")))
answer = equation[0]
for i in range(1, len(equation)) : 
    answer -= equation[i]
print(answer)