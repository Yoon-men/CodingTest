# 단어의 개수

sentence = list(input().split())
word = 0

for _ in range(len(sentence)) :         # "_" == 쓰지 않는다는 의미. 이거 써보려고 그냥 해봤다!
    word += 1

print(word)