import datetime
from datetime import timedelta

start = datetime.datetime(2024, 4, 11, 19, 15)
lecture = 1
day = timedelta(hours=24)


while lecture <= 32:
    if start.weekday() == 0 or start.weekday() == 3:
        print(f"Lecture {lecture:>2}: {start.strftime("%d %b %Y %H:%M")}")
        lecture += 1
    start += day
