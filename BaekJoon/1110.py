# 더하기 사이클
N = input()
if int(N) < 10 : 
    N = f"0{N}"
editedN = 0
cycledN = N
cycleNum = 0
while True : 
    editedN = str(int(cycledN[0]) + int(cycledN[1]))
    cycledN = f"{cycledN[1]}{editedN[-1]}"
    cycleNum += 1
    # print(f"N = {N} / cycledN = {cycledN} / cycleNum = {cycleNum}")       # Test code / please lock this line for submission.
    if int(cycledN) == int(N) : 
        break
print(cycleNum)