# 백준1475 : 방 번호
def joyGo(N) : 
    Di = {i : 0 for i in range(10)}
    for i in N : 
        i = int(i)
        if (i == 6) or (i == 9) : 
            if Di[6] < Di[9] : Di[6] += 1
            else : Di[9] += 1
        else : 
            Di[i] += 1

    return max(Di.values())


if __name__ == "__main__" : 
    N = input()
    print(joyGo(N))