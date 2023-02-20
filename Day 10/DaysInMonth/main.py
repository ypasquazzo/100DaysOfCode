# Using the code we wrote on Day 3 to check for leap years, write a program that tells you how many days there
# are in a given month using a function called {days_in_month()} which will take a year and a month as inputs.


def is_leap(year):
    if (year % 4) == 0:
        if (year % 100 == 0) and (year % 400 != 0):
            return False
        else:
            return True
    else:
        return False


def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(y):
        month_days[1] = 29
    return month_days[m - 1]


days = days_in_month(int(input("Enter a year: ")), int(input("Enter a month: ")))
print(days)
