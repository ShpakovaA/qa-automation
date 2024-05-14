# Sorting list of dates

# dates = ['14-Dec', '13-Apr', '12-Apr', '31-Dec', '1-Jan', '12-Jan', '10-Dec', '14-May']
dates = ['1-Dec', '02-Dec', '3-Dec', '5-Dec', '06-DEC', '7-Dec', '8-Dec', '9-Dec', '10-dec', '11-Dec', '12-Dec', '13-Dec']

months = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12
}

sorted_dates = sorted(dates, key=lambda date: (months[date.split("-")[1].lower()], int(date.split("-")[0])))

print(sorted_dates)  #  ['1-Jan', '12-Jan', '12-Apr', '13-Apr', '14-Dec', '31-Dec']
