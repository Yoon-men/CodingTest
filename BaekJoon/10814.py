# 나이순 정렬
N = int(input())
members = []
for i in range(N) : 
    age, name = map(str, input().split())
    age = int(age)
    members.append((age, name))
members.sort(key = lambda x : x[0])
for i in range(len(members)) : 
    print(f"{members[i][0]} {members[i][1]}")