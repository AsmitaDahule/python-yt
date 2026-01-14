year = int(input("\nenter year"))
month = int(input("\nenter month like 1/2/3...."))



month_days = {
  1 : 31,
  2 : 28,
  3 : 31,
  4 : 30,
  5 : 31,
  6 : 30,
  7 : 31,
  8 : 31,
  9 : 30,
  10 : 31,
  11 : 30,
  12 : 31
}


def is_leap(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def no_of_days(year, month):
    days = month_days[month]
    res = is_leap(year)
    if res == True:
        if month == 2:
            print(f"In {year} year month {month} there are 29 days")
        else:
            print(f"In {year} year month {month} there are {days} days")
    else:
        print(f"In {year} year month {month} there are {days} days")

          


no_of_days(year, month)