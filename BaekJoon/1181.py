# 단어 정렬
import sys
input = sys.stdin.readline
N = int(input())
word = []
for _ in range(N) : 
    word.append(input().strip())

word = list(set(word))
word.sort()
word.sort(key = len)

for i in word : 
    print(i)