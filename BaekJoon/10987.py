# 백준10987 : 모음의 개수
import sys
input = sys.stdin.readline

word = input().strip()
vowel = "aeiou"
num = 0

for i in word : 
    if i in vowel : 
        num += 1
print(num)