# 백준4673 : 셀프 넘버
originalNum = list(range(1, 10001))
newNum = []

for i in range(1, 10001) : 
    for j in str(i) : 
        i += int(j)
    newNum.append(i)

selfNum = sorted(set(originalNum) - set(newNum))

for i in selfNum : 
    print(i)