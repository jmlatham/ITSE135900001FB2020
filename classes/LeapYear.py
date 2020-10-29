class LeapYear:
  def __init__(self):
      pass

  def determineYearStatus(self, year):
    # if  not isinstance(year, int):
    #   return "invalid data"
    try:
      yearInt = int(year)

      if yearInt < 1582:
        return "Not within the Gregorian calendar period!"
      elif yearInt % 4 != 0:
        return "Common year"
      elif yearInt % 100 != 0:
        return "Leap year"
      elif yearInt % 400 != 0:
        return "Common year"
      else:
        return "Leap year"
    except:
        return "invalid data"
      
  def determineYearStatusNew(self, year):
    try:
      yearInt = int(year)

      if yearInt < 1582:
        return "Not within the Gregorian calendar period!"
      elif yearInt % 4 != 0 or (yearInt % 4 == 0 and yearInt % 100 == 0 and yearInt % 400 != 0):
        return "Common year"
      else:
        return "Leap Year"
    except:
      return "invalid data"

if __name__ == "__main__":
  while True:
    ly = LeapYear()
    year = input("Year: ")
    try:
        year = int(year)
    except:
        break
    print("old:", ly.determineYearStatus(year))
    print("new:", ly.determineYearStatusNew(year))

