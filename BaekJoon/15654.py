# 백준15654 : N과 M (5)
def joyGo(depth) : 
    if depth == M : 
        print(" ".join(map(str, box)))
        return
    for num in Li : 
        if num in box : 
            continue
        box.append(num)
        joyGo(depth+1)
        box.pop()

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = sorted(list(map(int, input().split())))

    box = []
    joyGo(0)