# from classes.ExampleClass import ExampleClass
# from Labs import Labs
# from classes.LeapYear import LeapYear
# from classes.BitwiseOperator import BitwiseOperator
# from classes.DecimalToBinary import DecimalToBinary
# from classes.ClassWork import ClassWork
from classes.FunctionsLessons import FunctionsLessons
from classes.OlderClassWork import OlderClassWork
from classes.InstanceVariables import InstanceVariables
from classes.FileClass import FileClass
from classes.JSONVehicles import JSONVehicles
from classes.functions import displayDictionaryMenu, getMenuChoice, myGlobalVariableTest, printRandomIntegers, runGame, runDataStructures, printDescriptions, runMathTest, listMathMethods, ceilFloorTrunc, printPlatformInformation, exceptionsTests
from classes.Labs5 import Labs5

from classes.RegularExpressions import RegularExpressions

funLess = FunctionsLessons()

def runOlderClassWork():
  ocw = OlderClassWork()
  menu = {"1":"First Chess Trial","2":"List Sorting Test","3":"List Test 1","4":"Bitwise Operator Test","5":"Decimal To Binary Converter","6":"Leap Year Test","7":"if elif Statement Test","8":"Print with different Types Test","9":"First if Statement Test","10":"Variable Test 1","11":"Module 2 Lab 2.1.1.7","12":"ExampleClass Test 1","13":"ExampleClass Test 2","101":"Making Functions","102":"Positional and Keyword Arguments","103":"Using None","104":"Strange Function","105":"Showing Function Scope","106":"Using Global Keyword","107":"Changing Variables within a function","109":"Create and Print Tuples","1010":"Using Tuples","1011":"Tuple Immutability", "1012":"Adding and Multiplying Tuples","1013":"Creating and using Dictionaries","1014":"Calculating Scores Example", "1015":"Print Random Integers","1016":"Run Game", "1017":"Test Data Structures", "1018":"Print Method Descriptions","1019":"Run Math module test", "1020":"Print Math module components","1021":"Test floor(), ceil(), trunc() from the math module","1022":"Print Platform information","2023":"Exceptions Tests","2025":"File Stream","2026":"File per character","2027":"File per line with per character printing","2028":"File per line","2029":"File per line characters separated by dash","2030":"Write Files","2031":"Files and Directories","2050":"new file program","0":"Quit"}
  while True:
    displayDictionaryMenu(menu, "OLD CODE")
    menuChoice = getMenuChoice()
    if menuChoice == 0:
      break
    elif menuChoice == 1:
      ocw.runFirstChessTrial()
    elif menuChoice == 2:
      ocw.runListSortingTests()
    elif menuChoice == 3:
      ocw.runListTest1()
    elif menuChoice == 4:
      ocw.runBitwiseOperatorTest()
    elif menuChoice == 5:
      ocw.runDecimalToBinaryConverter()
    elif menuChoice == 6:
      ocw.runLeapYearTest()
    elif menuChoice == 7:
      ocw.testIf_ElIfStatements()
    elif menuChoice == 8:
      ocw.testPrintWithDifferentTypes()
    elif menuChoice == 9:
      ocw.runFirstIfStatementTest()
    elif menuChoice == 10:
      ocw.runVariablesTest1()
    elif menuChoice == 11:
      ocw.runModule2Lab2_1_1_7()
    elif menuChoice == 12:
      ocw.useExampleClass1()
    elif menuChoice == 13:
      ocw.useExampleClass2()
    elif menuChoice == 14:
      ocw.testVehicles()
    elif menuChoice == 101:
      funLess.makingFunctions()
    elif menuChoice == 102:
      funLess.positionalKeywordArguments()
    elif menuChoice == 103:
      funLess.usingNone()
    elif menuChoice == 104:
      funLess.strangeFunction()
    elif menuChoice == 105:
      funLess.showScope()
    elif menuChoice == 106:
      funLess.keywordGlobal()
      print("========================")
      var = 1
      print("before calling myGlobalVariableTest():", var)
      myGlobalVariableTest()
      print("after calling myGlobalVariableTest():", var, end="\n\n\n\n")
    elif menuChoice == 107:
      funLess.changeVariableWithinFunction()
    elif menuChoice == 109:
      funLess.createAndPrintTuples()
    elif menuChoice == 1010:
      funLess.usingTuples()
    elif menuChoice == 1011:
      funLess.tupleImmutability() 
    elif menuChoice == 1012:
      funLess.addingAndMultiplyingTuples()
    elif menuChoice == 1013:
      funLess.creatingDictionaries()
    elif menuChoice == 1014:
      funLess.calculatingScoresExample()
    elif menuChoice == 1015:
      print("\n" * 3)
      printRandomIntegers(10, 100)
      print("\n" * 3)
    elif menuChoice == 1016:
      print("\n" * 3)
      runGame()
      print("\n" * 3)
    elif menuChoice == 1017:
      print("\n" * 3)
      runDataStructures()
      print("\n" * 3)
    elif menuChoice == 1018:
      print("\n" * 3)
      printDescriptions()
      print("\n" * 3)
    elif menuChoice == 1019:
      print("\n" * 3)
      runMathTest()
      print("\n" * 3)
    elif menuChoice == 1020:
      print("\n" * 3)
      listMathMethods()
      print("\n" * 3)
    elif menuChoice == 1021:
      print("\n" * 3)
      ceilFloorTrunc()
      print("\n" * 3)
    elif menuChoice == 1022:
      print("\n" * 3)
      printPlatformInformation()
      print("\n" * 3)
    elif menuChoice == 2023:
      print("\n" * 3)
      exceptionsTests()
      print("\n" * 3)
    elif menuChoice == 2025:
      print("\n" * 3)
      # import classes.FileClass
      fileClass = FileClass()
      fileClass.readFirstFile()
      print("\n" * 3)
      
    elif menuChoice == 2026:
      print("\n" * 3)
      # import classes.FileClass
      fileClass = FileClass()
      
      fileClass.readSecondFile()
      print("\n" * 3)
      
    elif menuChoice == 2027:
      print("\n" * 3)
      # import classes.FileClass
      fileClass = FileClass()
      
      fileClass.readThirdFile()
      print("\n" * 3)
      
    elif menuChoice == 2028:
      print("\n" * 3)
      # import classes.FileClass
      fileClass = FileClass()
      
      fileClass.readLinesCode(False)
      print("\n" * 3)

    elif menuChoice == 2029:
      print("\n" * 3)
      # import classes.FileClass
      fileClass = FileClass()
      
      fileClass.readLinesCode(True)
      print("\n" * 3)

    elif menuChoice == 2030:
      print("\n" * 3)
      fileClass = FileClass()
      fileClass.writeFile()
      print("\n" * 3)

    elif menuChoice == 2031:
      print("\n" * 3)
      fileClass = FileClass()
      fileClass.filesAndDirectories()
      print("\n" * 3)
    elif menuChoice == 2050:
      from classes.FileManipulator import FileManipulator

      fMan = FileManipulator()
      fMan.run()


menu = {"1":"Lab 5.1.6.4","2":"Lab 5.1.9.18","3":"Lab 5.1.10.6","4":"RegularExpressions","5":"Print Regular Expression information","6":"File Manipulator","14":"Vehicles Test","20":"Class Levels","21":"JSON Vehicle file creator","22":"Read JSON file","2024":"Instance variables vs Class variables","1000":"Car Dealership","108":"Run older code","0":"Quit", "5000":"Dealership"}

while True:
  displayDictionaryMenu(menu, "MAIN")
  menuChoice = getMenuChoice()
  if menuChoice == 0:
    break
  elif menuChoice == 108:
    runOlderClassWork()
  elif menuChoice == 1:
    lab5 = Labs5()
    lab5.lab5_1_6_4()
  elif menuChoice == 2:
    lab5 = Labs5()
    lab5.lab5_1_9_18()
  elif menuChoice == 3:
    lab5 = Labs5()
    lab5.lab5_1_10_6()
  elif menuChoice == 4:
    regEx = RegularExpressions()
    regEx.runREMethods()
  elif menuChoice == 5:
    regEx = RegularExpressions()
    regEx.printREInformation()
  elif menuChoice == 6:
    from classes.FileManipulator import FileManipulator

    fMan = FileManipulator()
    fMan.run()
  elif menuChoice == 14:
    ocw = OlderClassWork()
    ocw.testVehicles()
  elif menuChoice == 2024:
    print("\n" * 3)
    exampleObject1 = InstanceVariables()
    print("exampleObject1 dict:\n", exampleObject1.__dict__, "\n\tcounter:", exampleObject1.counter, "\n\tclassCounter:", exampleObject1.classCounter)
    
    exampleObject2 = InstanceVariables(2)
    exampleObject2.setSecond(3)
    print("exampleObject2 dict:\n", exampleObject2.__dict__, "\n\tcounter:", exampleObject2.counter, "\n\tclassCounter:", exampleObject2.classCounter)
    try:
      print("\texampleObject2.second:",exampleObject2.second)
    except AttributeError as e:
      print("Attempted to access exampleObject2.second - AttributeError: ", e)
    try:
      print(exampleObject2.__second)
    except AttributeError as e:
      print()
      print("Attempted to access exampleObject2.__second - AttributeError: ", e)
      print()

    exampleObject3 = InstanceVariables(3)
    exampleObject3.__third = 5 # not private
    exampleObject3.third = 5
    print("exampleObject3 dict:\n", exampleObject3.__dict__, "\n\tcounter:", exampleObject3.counter, "\n\tclassCounter:", exampleObject3.classCounter)

    print("\n" * 3)

    print("exampleObject1 dict:\n", exampleObject1.__dict__, "\n\tcounter:", exampleObject1.counter, "\n\tclassCounter:", exampleObject1.classCounter)
    print("exampleObject2 dict:\n", exampleObject2.__dict__, "\n\tcounter:", exampleObject2.counter, "\n\tclassCounter:", exampleObject2.classCounter)
    print("exampleObject3 dict:\n", exampleObject3.__dict__, "\n\tcounter:", exampleObject3.counter, "\n\tclassCounter:", exampleObject3.classCounter)
    # print(exampleObject2.__dict__, exampleObject2.counter, exampleObject2.classCounter)
    # print(exampleObject3.__dict__, exampleObject3.counter, exampleObject3.classCounter)
    print("\n" * 3)
  elif menuChoice == 21:
    jsonVehicles = JSONVehicles()
    if input("\nAre you sure you want to over write your current file? ") in ["Y","y"]:
      # jsonVehicles.createFile()
      jsonVehicles.createVehiclesFile()
      # print("File Recreated!\n\n")
    else:
      print("Ok. Maybe next time.\n\n")

  elif menuChoice == 22:
    jsonVehicles = JSONVehicles()
    if input("\nAre you sure you want to display the contents of your file? ") in ["Y","y"]:
      jsonVehicles.readFile("vehicles.json")
    else:
      print("Ok. Maybe next time.\n\n")

  elif menuChoice == 1000:
    from cardealership.Dealership import Dealership
    dealership = Dealership()
    dealership.runTest()

  elif menuChoice == 20:
    class Level1:
      varia1 = 100
      def __init__(self):
          self.var1 = 101

      def fun1(self):
          return 102
          
      def fun4(self):
          return 402


    class Level2(Level1):
        varia2 = 200
        def __init__(self):
            super().__init__()
            self.var2 = 201
        
        def fun2(self):
            return 202


    class Level3(Level2):
        varia3 = 300
        def __init__(self):
            super().__init__()
            self.var3 = 301

        def fun3(self):
            return 302

    obj = Level3()

    print(obj.varia1, obj.var1, obj.fun1())
    print(obj.varia2, obj.var2, obj.fun2())
    print(obj.varia3, obj.var3, obj.fun3())
    print(obj.fun4())

  elif menuChoice == 5000:
    from cardealership.Dealership import Dealership
    dealer = Dealership()
    dealer.displayMenu("dealership")
    
