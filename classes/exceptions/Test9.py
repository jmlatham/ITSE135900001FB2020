def RaisingAnError():
  print("\nraising an error")
  def badFun3(n):
      raise ZeroDivisionError
      # raise OverflowError
      # raise ValueError
    
  try:
      badFun3(0)
  except ArithmeticError:
      print("What happened? An error?")
  except:
    print("Other error")
  print("THE END.")




  print("\nusing the raise in except")
  def badFun4(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise # using raise like this can only be in the except
  try:
    badFun4(0)
  except ArithmeticError:
      print("I see!")
  print("THE END.")