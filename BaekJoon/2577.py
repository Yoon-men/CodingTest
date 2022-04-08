# 숫자의 개수

A = int(input(""))
B = int(input(""))
C = int(input(""))

ABC = A * B * C

ABC_List = list(str(ABC))
ABC_appearNum = [0] * 10

for i in range(10) : 
    if str(i) in ABC_List : 
        for j in range(len(ABC_List)) : 
            if ABC_List[j] == str(i) : 
                ABC_appearNum[i] += 1

for i in ABC_appearNum : 
    print(i)