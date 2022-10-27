def date(day, month, year):
    month_30 = [4, 6, 9, 11]
    month_31 = [1, 3, 5, 7, 8, 10, 12]

    if 0 < day < 31 and month in month_30:
        return True
    if 0 < day < 32 and month in month_31:
        return True
    if month == 2:
        if 0 < day <= 28:
            return True
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if 0 < day <= 29:
                return True
    return False

print(date(28, 2, -2001))      
