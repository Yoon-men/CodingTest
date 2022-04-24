# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokedex = []        # "포켓몬을 만나면 자동으로 기록해주는 하이테크한 도구란다!"
pokedex_Num = {}

for i in range(N) : 
    name = input().strip()
    pokedex.append(name)
    pokedex_Num[name] = i + 1

for _ in range(M) : 
    question = input().strip()
    if question.isdigit() : 
        print(pokedex[int(question) - 1])
    
    elif question.isalpha() : 
        print(pokedex_Num[question])