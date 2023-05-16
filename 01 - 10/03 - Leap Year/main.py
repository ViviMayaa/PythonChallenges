

def input():
    # 2000, 1992 and 2400 are leap years
    # 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
    return 2000


# ATTENTION! % when gives a 0 back is considered FALSE
# integer division 3//5 = 0
# float division 3/5 = 0.6
# remains division 4%4 = 0 False
def is_leap(year_leap):
    leap = False
    if not year_leap % 4:
        if year_leap % 100:
            leap = True
        elif not year_leap % 400:
            leap = True

    return leap


year = int(input())
print(is_leap(year))


