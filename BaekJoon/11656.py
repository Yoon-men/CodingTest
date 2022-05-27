# 접미사 배열
import sys
word = sys.stdin.readline().strip()
wordList = [[] for _ in range(len(word))]
for i in range(len(word)) : 
    if i == 0 : 
        wordList[i] = word
    else : 
        word = word[1:]
        wordList[i] = word
for i in sorted(wordList) : 
    print(i)