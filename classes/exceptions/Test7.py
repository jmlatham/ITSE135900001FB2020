from math import exp as EXP

def MultipleExceptionsHandled():
  print("\nMultiple exceptions handled")

  # ex = 1
  # while True:
  #     print(EXP(ex))
  #     ex *= 2

  try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
    ex = 1
    while True:
        print(EXP(ex))
        ex *= 2
  except ZeroDivisionError: # try to switch this with ArithmeticError
      print("You cannot divide by zero, sorry.")
  except OverflowError: # try to put this before the ArithmeticError
    print('The number is too big.')
  except ArithmeticError: # this keeps the ZeroDivisionError from being reached
      print("Arithmetic Problem!")
  except ValueError:
      print("You must enter an integer value.")
  except:
      print("Oh dear, something went wrong...")
  
  print("THE END.")