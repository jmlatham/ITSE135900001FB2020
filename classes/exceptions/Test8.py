def InsideErrorHandling():
  print("\nexception handled inside function")
  def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None
  print(badFun(0))
  print("THE END.")





def OutsideErrorHandling():
  print("\nexception handled outside function")
  def badFun2(n):
        return 1 / n
  try:
    badFun2(0)
  except ArithmeticError:
    print("Arithmetic Problem!")
  print("THE END.")