def UsingIfElseToHandleDataInput():
  print("\none way division by zero can be handled: using if/else")
  firstNumber = int(input("Enter the first number: "))
  secondNumber = int(input("Enter the second number: "))
  if secondNumber != 0:
      print(firstNumber / secondNumber)
  else:
      print("This operation cannot be done.")
  print("THE END.")