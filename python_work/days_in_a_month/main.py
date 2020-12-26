
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False  
    else:
      return True
  else:
    return False

def days_in_month(f_year, f_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  # month_serial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  # if is_leap(f_year):
  #   month_days[1] = 29
  # if f_month in month_serial:
  #   return month_days[month_serial.index(f_month)]
  
  if is_leap(f_year):
    month_days[1] = 29

  return month_days[f_month - 1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)















# Tests
import unittest

class MyTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(days_in_month(2018, 2), 28)

    def test_2(self):
        self.assertEqual(days_in_month(2020, 2), 29)

    def test_3(self):
        self.assertEqual(days_in_month(2019, 4), 30)

    def test_4(self):
        self.assertEqual(days_in_month(1045, 5), 31)

print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)