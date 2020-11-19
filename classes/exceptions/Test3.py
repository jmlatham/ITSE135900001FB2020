def IndexOutOfRange(position):
  print("\nindex out of range exception")
  list = [1, 2, 3, 4, 5, 6]
  if position < len(list):
    x = list[position]
    print("x = ", x)