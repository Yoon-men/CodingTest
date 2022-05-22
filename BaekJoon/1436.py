# 영화감독 숌
import sys
input = sys.stdin.readline
N = int(input())
counting = 0
doomsday = 666
while True : 
    if "666" in str(doomsday) : 
        counting += 1
    if N == counting : 
        print(doomsday)
        break
    doomsday += 1