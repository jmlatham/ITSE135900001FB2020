def ShowingCodeNotExecuted():
  print("\nanother exception handled but remainder of code not executed")
  try:
    print("1")
    x = 1 / 0
    print("2")
    print("36")
    
  except:
      print("Oh dear, something went wrong...")
  print("3")
  for i in range(10):
      print(i, i*2)