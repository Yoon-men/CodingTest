# 백준1874 : 스택 수열
import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
stack = []
answer = []
check = True

for _ in range(n) : 
    num = int(input())

    while cnt <= num : 
        stack.append(cnt)
        answer.append("+")
        cnt += 1
    
    if stack[-1] == num : 
        stack.pop()
        answer.append("-")
    else : 
        check = False

if check == True : 
    for i in answer : 
        print(i)
else : 
    print("NO")