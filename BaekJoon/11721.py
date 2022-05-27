# 열 개씩 끊어 출력하기
import sys
word = list(sys.stdin.readline().strip())
while len(word) > 0 : 
    print("".join(str(i) for i in word[:10]))
    del word[:10]