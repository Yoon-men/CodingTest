# 균형 잡힌 세상
while True : 
    sentence = input()
    box = []

    if sentence == "." : 
        break

    for i in sentence : 
        if i == "(" or i == "[" : 
            box.append(i)
        elif i == ")" : 
            if len(box) != 0 and box[-1] == "(" : 
                box.pop()
            else : 
                box.append(i)
                break
        elif i == "]" : 
            if len(box) != 0 and box[-1] == "[" : 
                box.pop()
            else : 
                box.append(i)
                break
    
    if len(box) == 0 : 
        print("yes")
    else : 
        print("no")