from .ExampleClass import ExampleClass
from .Labs import Labs
from .LeapYear import LeapYear
from .BitwiseOperator import BitwiseOperator
from .DecimalToBinary import DecimalToBinary
from .ClassWork import ClassWork

class OlderClassWork:
  bwo = None
  def __init__(self):
    self.bwo = BitwiseOperator()
  
  
  def runFirstChessTrial(self):
    def printBoard():
      for column in range(0,len(board)):
        for row in range(0,len(board[column])):
          print(board[column][row], end=", ")
        print()
      print("\n\n")

    def printBoardDictionary(dictionaryVariable):
      print("A","B","C")
      for row in range(1,9):
        print(row)

        for column in ["A","B"]:
          print(column, end=" ")
          print(dictionaryVariable[column+"-"+str(row)], end=", ")
        print()


    EMPTY = "-"
    WPieces = ["W-ROOK", "W-KNIGHT", "W-BISHOP", "W-QUEEN", "W-KING", "W-PAWN"]
    BPieces = ["B-ROOK", "B-KNIGHT", "B-BISHOP", "B-QUEEN", "B-KING", "B-PAWN"]
    board = []

    for i in range(8):
        row = [EMPTY for i in range(8)]
        board.append(row)

    board[0][0] = WPieces[0]
    board[0][1] = WPieces[1]
    board[0][2] = WPieces[2]
    board[0][3] = WPieces[3]
    board[0][4] = WPieces[4]
    board[0][5] = WPieces[2]
    board[0][6] = WPieces[1]
    board[0][7] = WPieces[0]

    # [board[1][column] = PAWN for column in range(0,8)]
    for column in range(0,8):
      board[1][column] = WPieces[5]
    for column in range(0,8):
      board[6][column] = BPieces[5]

    board[7][0] = BPieces[0]
    board[7][1] = BPieces[1]
    board[7][2] = BPieces[2]
    board[7][3] = BPieces[3]
    board[7][4] = BPieces[4]
    board[7][5] = BPieces[2]
    board[7][6] = BPieces[1]
    board[7][7] = BPieces[0]

    printBoard()
    #move pawn one space
    board[5][0] = BPieces[5]
    board[6][0] = EMPTY

    printBoard()


    # for Mike's question!!!!!


    board = {"A-1":"Rook","B-1":"Knight","A-8":"-"}

    board = {"A-1":WPieces[0],"A-3":EMPTY,"A-4":EMPTY,"A-5":EMPTY,"A-6":EMPTY,"A-7":EMPTY,"A-8":BPieces[0],"B-1":WPieces[0], "B-2":WPieces[1],"B-3":EMPTY,"B-4":EMPTY,"B-5":EMPTY,"B-6":EMPTY,"B-7":EMPTY,"B-8":BPieces[1]}

    # print(board)
    board["A-2"] = "Rook"
    board["A-1"] = EMPTY
    # print (board)
    printBoardDictionary(board)
    position = input("What position: ")
    piece = input("What piece: ")

    print(board[position])
    print(piece)
    printBoardDictionary(board)


  def runListSortingTests(self):
    classWork = ClassWork()

    classWork.runCharacterSortLab()
    classWork.runSortFloat()
    classWork.runSortBubbleFloat()
    classWork.runOriginalSortLab()
    
    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    rows = [x for x in range(1,9)]
    print(columns)
    print(rows)
    for i in rows:
      for j in columns:
        print(j,'-',i, end="\t")
      print()

    columns = [[x for x in range(1,9)], [x for x in range(1,9)], [x for x in range(1,9)]]
    print(columns)

    columns[0][0] = "Rook"
    columns[0][1] = "Bishop"
    for i in range(3):
      for j in range(8):
        print(columns[i][j], end="\t")
      print()

  def runListTest1(self):
    testList = [10,9,8,7,6,5]
    print(testList," - ",len(testList))
    print(testList[5])
    for i in range(0,5):
      testList.append(i)
    print("testList contents: ", testList)


  # bwo = BitwiseOperator()
  # showAndValue(3,4)
  # https://en.wikipedia.org/wiki/Bitwise_operation#NOT
  def showAndValue(self, value1, value2):
    print("AND: ", value1, "&", value2, "=", self.bwo.And(value1,value2), end="\t")
    print(DecimalToBinary(value1), "&", DecimalToBinary(value2), "=", DecimalToBinary(self.bwo.And(value1,value2)))

  def showOrValue(self,value1, value2):
    print("OR:  ", value1, "|", value2, "=", self.bwo.Or(value1,value2), end="\t")
    print(DecimalToBinary(value1), "|", DecimalToBinary(value2), "=", DecimalToBinary(self.bwo.Or(value1,value2)))
    
  def showXorValue(self,value1, value2):
    print("XOR: ", value1, "^", value2, "=", self.bwo.Xor(value1,value2), end="\t")
    print(DecimalToBinary(value1), "^", DecimalToBinary(value2), "=", DecimalToBinary(self.bwo.Xor(value1,value2)))
    
  def showNotValue(self,value):
    print("NOT: ", "~", value, "=", ~value, end="\t")
    print("~", value, "=", self.bwo.Not(value), end="\t")
    print("~",DecimalToBinary(value), "=", self.bwo.Not(value))
    
  def showLeftShiftValue(self,value1, value2):
    print("Left Shift:  ", value1, "<<", value2, "=", self.bwo.LeftShift(value1,value2), end="\t")
    print(DecimalToBinary(value1), "<<", value2, "=", DecimalToBinary(self.bwo.LeftShift(value1,value2)))
    
  def showRightShiftValue(self,value1, value2):
    print("Right Shift: ", value1, ">>", value2, "=", self.bwo.RightShift(value1,value2), end="\t")
    print(DecimalToBinary(value1), ">>", value2, "=", DecimalToBinary(self.bwo.RightShift(value1,value2)))
    

  def runBitwiseOperatorTest(self):
    if input("Would you like to run the Bitwise Operator tester? ").lower() in "y, yes":
      while True:
        firstRangeStart  = input("Please enter the start of your first range: ")
        firstRangeStop   = input("Please enter the end of your first range: ")
        secondRangeStart = input("Please enter the start of your second range: ")
        secondRangeStop  = input("Please enter the end of your second range: ")
        shiftValue       = input("Please enter a shift value: ")

        try:
          firstRangeStart  = int(firstRangeStart)
          firstRangeStop   = int(firstRangeStop)
          secondRangeStart = int(secondRangeStart)
          secondRangeStop  = int(secondRangeStop)
          shiftValue       = int(shiftValue)
        except:
          print("The range and shift values must be integers. Please try again.")
          continue

        for i in range(firstRangeStart, firstRangeStop+1, -1):
          print("--------------------------")

          for j in range(secondRangeStart, secondRangeStop+1):
            self.showAndValue(i, j)
            self.showOrValue(i, j) 
            self.showXorValue(i, j) 

          print("   ***   ***   ***   ")
          self.showNotValue(i) 
          self.showLeftShiftValue(i, shiftValue)
          self.showRightShiftValue(i, shiftValue) 
          print("--------------------------")

        if input("Would you like to display another range? ").lower() not in "y, yes":
          break



  def runDecimalToBinaryConverter(self):
    if input("Would you like to run the Decimal to Binary convertor? ").lower() in "y, yes":
      print("To exit the code enter an non-integer value.")
      decimal = 0
      while True:
        try:
          decimal = int(input("Decimal:"))
        except:
          break
        print(DecimalToBinary(decimal))
        print(bin(decimal),"--->",bin(decimal).replace("0b",""))
        print(~decimal)


  def runLeapYearTest(self):
    while True:
      ly = LeapYear(self)
      year = input("Year: ")
      try:
          year = int(year)
      except:
          break
      print("old:", ly.determineYearStatus(year))
      print("new:", ly.determineYearStatusNew(year))


  def testIf_ElIfStatements(self):
    anything = input("Enter a number: ")
    something = anything * 2.0
    print(anything, "to the power of 2 is", something)

    userAge = int(input("Enter Your Age: "))
    userName = input("Enter Your Name: ")
    favoriteAge = 54

    category1CutOff = 18
    category2CutOff = 13

    if userAge >= category1CutOff:
      print("Hello, ", userName)
      print("Welcome to our program at Category 1. You are our priority!")
      if (userName.lower() == "smith" or userName.lower() == "bill") and userAge==favoriteAge:
        print("you are my favorite person.")
    elif userAge >= category2CutOff:
      print("Yo!", userName)
      print("You are in Category 2. ")
      if userName.lower() == "jones":
        print("you are my favorite person.")
    elif userAge >= 3:
      print("hi little camper")
      print("you are ", userAge, "years old")
    else:
      print("Get out of here, you are not old enough.")

  def testPrintWithDifferentTypes(self):
    var = 1
    account_balance = 1000.0
    client_name = 'John Doe'
    print(var, account_balance, client_name)

  def runFirstIfStatementTest(self):
    print(True > False)
    print(True < False)
    AgeOfCat = input("What is the age of your cat?")
    if AgeOfCat == 0:
      print("Sorry can't commute")
    else:
      try:
        print(1/int(AgeOfCat))
      except:
        print("The age of the Cat must be an integer greater than 0.")

  def runVariablesTest1(self):
    print("helloooooo,","nurse!!!", sep=" ", end="\n")
    print('Yako said, "Hello, nurse"')
    print("No he didn't!")
    print('No he didn\'t')
    print("H", "E", "L" "L", "O", sep="-")

    print(123)
    print('c')

    print(11111111)
    print(11,111,111)
    print(11_111_111)
    print("11,111,111")

    variable1 = 11111111
    variable2 = "11111111"
    print(variable1)
    print(variable2)
    print(variable1*3)
    print(variable2*3)
    print(variable1*variable2)

  def runModule2Lab2_1_1_7(self):
    module2 = Labs()
    module2.runLab2_1_1_7()

  def useExampleClass1(self):
    exampleClass = ExampleClass("Marshall", 3)
    print(exampleClass.doubleMyAge())
    print(exampleClass.name)
    exampleClass.age = 103
    exampleClass.name = "John"
    print(exampleClass.name, exampleClass.age)

    #print(exampleClass.privateVariable1)
    #print(exampleClass.__privateVariable1)

  def useExampleClass2(self):
    eClass = ExampleClass("me", 13)
    print("My First Program in Python!!")
    print(eClass.doubleMyAge())
    print("\n""private values:")
    print(eClass.getPrivateVariable1())
    eClass.setPrivateVariable1("private Variable 1 has changed")

    print(eClass.getPrivateVariable1())
    print("\nnow working with \"#2\"\n")
    print(eClass.getPrivateVariable2())

    eClass.setPrivateVariable2("abc")
    print(eClass.getPrivateVariable2())
    eClass.setPrivateVariable2("def")
    print(eClass.getPrivateVariable2())
    
    flamawhammer = ExampleClass("",15)
    print("------------")
    print(flamawhammer.doubleMyAge())
    

    print("\n""public values:")
    print(eClass.name, eClass.age)

    print()
    print("Added GitHub")


  def testVehicles(self):
    from .vehicles.Vehicle import Vehicle
    from .vehicles.LandVehicle import LandVehicle
    from .vehicles.SeaVehicle import SeaVehicle
    from .vehicles.AirVehicle import AirVehicle
    from .vehicles.SpaceVehicle import SpaceVehicle
    from .vehicles.WheeledVehicle import WheeledVehicle
    from .vehicles.TrackedVehicle import TrackedVehicle
    from .vehicles.HoverCraftVehicle import HoverCraftVehicle
    from .vehicles.Car import Car
    from .vehicles.Truck import Truck

    vehicle = Vehicle()
    landVehicle = LandVehicle("LAND", "AVAILABLE")
    seaV = SeaVehicle("SEA", "AVAILABLE")
    airV = AirVehicle("AIR", "AVAILABLE")
    spaceV = SpaceVehicle("SPACE", "AVAILABLE")
    wheeledVechicle = WheeledVehicle("WHEELED", "AVAILABLE")
    trackedV = TrackedVehicle("TRACKED", "AVAILABLE")
    hcV = HoverCraftVehicle("HOVERCRAFT", "AVAILABLE")
    car1 = Car("CAR","AVAILABLE","honk honk")
    car2 = Car("CAR","AVAILABLE","beep beep")
    truck1 = Truck("TRUCK","AVAILABLE","hooey hooey")

    vehicle.blowHorn()
    landVehicle.blowHorn()
    wheeledVechicle.blowHorn()
    seaV.blowHorn()
    airV.blowHorn()
    spaceV.blowHorn()
    trackedV.blowHorn()
    hcV.blowHorn()
    car1.blowHorn()
    car2.blowHorn()
    truck1.blowHorn()

    print(isinstance(car1, Vehicle))
    print(isinstance(car1, SeaVehicle))
    print(issubclass(Car, Vehicle))
    print(issubclass(WheeledVehicle, SpaceVehicle))