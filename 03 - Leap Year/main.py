

def input():
    # 2000, 1992 and 2400 are leap years
    # 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
    return 1992


# ATTENTION! % when gives a 0 back is considered FALSE
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
