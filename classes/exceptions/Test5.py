def UsingTryExceptToHandleZeroDivision():
  print("\nusing try/except to handle zero division")
  
  try:
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))
    list = []
    print(list[3])
    print(firstNumber / secondNumber)
  except:
      print("This operation cannot be done.")
  print("THE END.")