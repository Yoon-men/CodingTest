# 팰린드롬수
while True : 
    N = input()

    if N == "0" : 
        break
    
    if N == N[::-1] :       # If N = "123" => N[::-1] = "321"
        print("yes")
    else : 
        print("no")