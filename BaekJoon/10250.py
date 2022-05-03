# ACM 호텔
T = int(input())
for _ in range(T) : 
    floors, rooms, guest = map(int, input().split())
    room = guest//floors + 1
    if guest % floors == 0 : 
        print(floors*100 + room - 1)
    else : 
        print(guest%floors*100 + room)