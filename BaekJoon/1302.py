# 백준1302 : 베스트셀러
import sys ; input = sys.stdin.readline
books = {}
for _ in range(int(input())) : 
    book = input().strip()
    if book in books : books[book] += 1
    else : books[book] = 1
n = max(books.values())
bs = []
for i in books : 
    if books[i]==n : bs.append(i)
print(sorted(bs)[0])