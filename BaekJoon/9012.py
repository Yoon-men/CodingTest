# 괄호
T = int(input())
for _ in range(T) : 
    data = list(input())
    form = 0
    # ( -> 출현 시 form += 1
    # ) -> 출현 시 form -= 1

    # if ())   [불완전형태] -> form = -1
    # if ())(  [불완전형태] -> form = 0 -> form이 -1이 되는 순간 불완전형태
    # if ()(() [불완전형태] -> form = 1
    for i in data : 
        if i == "(" : 
            form += 1
        
        elif i == ")" : 
            form -= 1
        
        if form < 0 : 
            print("NO")
            break
    
    if form > 0 : 
        print("NO")
    
    elif form == 0 : 
        print("YES")