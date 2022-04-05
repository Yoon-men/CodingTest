def solution(n, lost, reserve):
    
    for i in reserve : 
        if i in lost : 
            lost.remove(i)
            reserve.remove(i)
    
    lost.sort()
    reserve.sort()
    
    for i in lost : 
        if i in reserve : 
            reserve.remove(i)
        
        elif (i - 1) in reserve : 
            reserve.remove(i - 1)

        elif (i + 1) in reserve : 
            reserve.remove(i + 1)

        else : 
            n -= 1

    print(n)        # Test code / please delete this line for submission.
    return n

solution(5, [2, 4], [1, 3, 5])      # Test code / please delete this line for submission.