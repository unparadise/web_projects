# Compare whether the number of days between two dates is greater than a given
# number

from datetime import date

def longerThanDays(date1, date2, length):
    delta = date2 - date1
    print(delta.days)
    if delta.days > length:
        # print('Your csv date file is more than ' + str(length) + ' days old.')
        return True
    else:
        # print('Your csv data file is less than ' + str(length) + ' days old.')
        return False


# Test
# longerThanDays(date(2021, 1, 10), date.today(), 30)