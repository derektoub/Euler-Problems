import time

def daysAndSundays(year, day):
    if len(year) == 1:
        for month in range(1,13):
            if month == 4 or month == 6 or month == 9 or month == 11:
                day += 30
            elif month == 2:
                if (year[0] % 4 == 0 and year[0] % 100 != 0) or year[0] % 400 == 0:
                    day += 29
                else:
                    day += 28
            else:
                day += 31
        return day
    elif len(year) == 2:
        count = 0
        for years in range(year[0], year[1] + 1):
            for month in range(1,13):
                if day % 7 == 2:
                    count += 1
                if month == 4 or month == 6 or month == 9 or month == 11:
                    day += 30
                elif month == 2:
                    if (years % 4 == 0 and years % 100 != 0) or years % 400 == 0:
                        day += 29
                    else:
                        day += 28
                else:
                    day += 31
        return count
    else:
        print "Please either put in one year, or the start year and end year in a list"
        exit(1)
start = time.time()
a = daysAndSundays([1900], 1) % 7 # a is the first day of 1901, which is a tuesday (= 2)
count = daysAndSundays([1901, 2000], a)
elapsed = time.time() - start
print count
print "%s seconds elapsed" % elapsed

