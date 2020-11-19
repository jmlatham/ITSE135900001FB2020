from math import sqrt as SQRT

def UsingAssert():
  try:
    print("\nassert keyword")
    x = float(input("Enter a number: "))
    assert x >= 0.0 # raises AssertionError if condition fails and code execution stops
    x = SQRT(x)
    print(x)
  except AssertionError:
    print("Assert worked!!")
  except ValueError:
    print("you entered bad data.")
  except:
    print("you found an error!")