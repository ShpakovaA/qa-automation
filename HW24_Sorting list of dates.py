# Sorting list of dates

dates = ['14-Dec', '12-Apr', '13-Apr', '31-Dec', '1-Jan', '12-Jan']

sorted_dates = sorted(dates, key=lambda date: date.split("-")[0], reverse=True)[::-1]


print(sorted_dates)  #  ['1-Jan', '12-Jan', '12-Apr', '13-Apr', '14-Dec', '31-Dec']


