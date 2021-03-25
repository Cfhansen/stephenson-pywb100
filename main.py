###solution to exercise 100 from ben stephenson's "the python workbook".

def is_leap_year(year):
  result = False
  if (not year % 400) or ((not year % 4) and (year % 100)):
    result = True
  return result

def monthdays(month, year):

  monthdays = { 1:  31,
                2:  28,
                3:  31,
                4:  30,
                5:  31,
                6:  30,
                7:  31,
                8:  31,
                9:  30,
                10: 31,
                11: 30,
                12: 31 }

  result = monthdays[month]
  if is_leap_year(year) and month == 2:
    result += 1
  return result

print("Enter the month: ")
month = int(input())
print('Enter the year: ')
year = int(input())

print(monthdays(month, year))
