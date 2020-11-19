class ClassWork:
  def __init__(self):
    pass
  

  def runCharacterSortLab(self):
    a = "A"
    b = "B"
    c = "C"
    d = " "
    e = "a"
    f = "b"
    g = "c"
    h = "!"
    i = "&"
    j = "%"

    lst = [a, b, c, d, e, f, g, h, i, j]
    print(lst)
    lst.reverse()
    print(lst)
    lst.sort()
    print(lst)

    for i in lst:
      print(i,ord(i),chr(ord(i)))
    if False:
      for i in range(1000):
        endCharacter = "\t"
        if i % 15 == 0:
          endCharacter = "\n"
        print(chr(i), end=endCharacter)
  
  def runSortFloat(self):
    myList = []
    swapped = True
    num = int(input("How many elements do you want to sort: "))
    print("PSYCH!!!! Enter float values (use a letter to quit).")

    # for i in range(num):
    #     val = float(input("Enter a list element: "))
    #     myList.append(val)

    while True:
      try:
        myList.append(float(input("Float value: ")))
      except:
        break

    while swapped:
        swapped = False
        for i in range(len(myList) - 1):
            if myList[i] > myList[i + 1]:
                swapped = True
                myList[i], myList[i + 1] = myList[i + 1], myList[i]

    print("\nSorted:")
    print(myList)

  def runSortBubbleFloat(self):
    myList = []
    swapped = True
    num = int(input("How many elements do you want to sort: "))
    print("PSYCH!!!! Enter float values (use a letter to quit).")

    # for i in range(num):
    #     val = float(input("Enter a list element: "))
    #     myList.append(val)

    while True:
      try:
        myList.append(float(input("Float value: ")))
      except:
        break

    while swapped:
        swapped = False
        for i in range(len(myList) - 1):
            if myList[i] > myList[i + 1]:
                swapped = True
                myList[i], myList[i + 1] = myList[i + 1], myList[i]

    print("\nSorted:")
    print(myList)
  
  def runOriginalSortLab(self):
    myList = [8, 10, 6, 2, 4] # list to sort
    print(myList)
    print("Length:",len(myList))
    print("Range:",range(len(myList)-1))
    for i in range(len(myList) - 1): # we need (5 - 1) comparisons
        print("element:",i, "data:",myList[i])
        if myList[i] > myList[i + 1]: # compare adjacent elements
            myList[i], myList[i + 1] = myList[i + 1], myList[i] # if we end up here it means that we have to swap the elements
    print(myList)

    for i in ["A","B","C"]:
      print(i)
    print("--------------")
    print("--------------")

    myList = [8, 10, 6, 2, 4] # list to sort
    swapped = True # it's a little fake - we need it to enter the while loop

    while swapped:
        swapped = False # no swaps so far
        for i in range(len(myList) - 1):
            if myList[i] > myList[i + 1]:
                swapped = True # swap occured!
                myList[i], myList[i + 1] = myList[i + 1], myList[i]
                print(myList)
    print(myList)