# 단어 공부

word = input()
word = list(word)
word.sort()

for i in range(len(word)) : 
    word[i] = word[i].upper()

alphabet = []

for i in range(len(word)) : 
    if i == 0 : 
        alphabet.append(word[i])
    
    else : 
        if word[i] != word[i - 1] : 
            alphabet.append(word[i])

alphabetNum = [0] * len(alphabet)

for i in word : 
    alphabetIndex = alphabet.index(i)
    alphabetNum[alphabetIndex] += 1

alphabetMode = []

for i in range(len(alphabetNum)) : 
    if alphabetNum[i] == max(alphabetNum) : 
        alphabetMode.append(alphabet[i])

if len(alphabetMode) >= 2 : 
    print("?")

else : 
    print(alphabetMode[0])