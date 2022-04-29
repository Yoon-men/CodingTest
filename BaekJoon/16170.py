# 오늘의 날짜는?
import datetime
currentTime = datetime.datetime.now() - datetime.timedelta(hours=9)
print(currentTime.year)
print(currentTime.month)
print(currentTime.day)