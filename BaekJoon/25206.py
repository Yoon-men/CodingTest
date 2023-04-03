# 백준25206 : 너의 평점은
import sys; input = sys.stdin.readline

rating_dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0}
gradeSum, gradeXratingSum = 0, 0

for _ in range(20) : 
    __, grade, rating = input().split(); grade = float(grade)
    if rating == "P" : continue
    gradeSum += grade
    gradeXratingSum += grade*rating_dict[rating]

print(f"{gradeXratingSum/gradeSum:.6f}")