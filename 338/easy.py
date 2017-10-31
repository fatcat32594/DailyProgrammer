#!/bin/python

import sys

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def zellers(year, month, dom):
    if (month == 1 or month == 2):
        year -= 1
        month += 12
    century = year // 100
    domVariation = 13*(month+1) // 5
    leapYear = year // 4
    century = year // 100
    leapCentury = century // 4
    dow = (dom + domVariation + year + leapYear - century + leapCentury) % 7
    print(days[dow])

    
if __name__ == "__main__":
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    zellers(year, month, day)
