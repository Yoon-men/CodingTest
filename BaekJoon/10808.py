# 알파벳 개수
import sys
word = sys.stdin.readline()
alphabet = "abcdefghijklmnopqrstuvwxyz"
numList = [0] * len(alphabet)
count = 0
for i in alphabet : 
    if i in word : 
        for j in word : 
            if j == i : 
                numList[count] += 1
    count += 1
print(" ".join(str(i) for i in numList))