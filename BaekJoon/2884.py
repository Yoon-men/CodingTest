# 알람 시계

H, M = list(map(int, input().split()))

time = 60*H + M
time -= 45

if time >= 0 : 
    H = time // 60
    M = time % 60
    print(f"{H} {M}")

else : 
    time = 1440 + time
    H = time // 60
    M = time % 60
    print(f"{H} {M}")