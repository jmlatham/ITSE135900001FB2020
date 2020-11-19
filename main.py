# from classes.ExampleClass import ExampleClass
# from Labs import Labs
# from classes.LeapYear import LeapYear
# from classes.BitwiseOperator import BitwiseOperator
# from classes.DecimalToBinary import DecimalToBinary
# from classes.ClassWork import ClassWork
from classes.FunctionsLessons import FunctionsLessons
from classes.OlderClassWork import OlderClassWork
from classes.functions import *
import random


def runOlderClassWork():
  ocw = OlderClassWork()
  menu = {"1":"First Chess Trial","2":"List Sorting Test","3":"List Test 1","4":"Bitwise Operator Test","5":"Decimal To Binary Converter","6":"Leap Year Test","7":"if elif Statement Test","8":"Print with different Types Test","9":"First if Statement Test","10":"Variable Test 1","11":"Module 2 Lab 2.1.1.7","12":"ExampleClass Test 1","13":"ExampleClass Test 2","14":"Vehicles Test","101":"Making Functions","102":"Positional and Keyword Arguments","103":"Using None","104":"Strange Function","105":"Showing Function Scope","106":"Using Global Keyword","107":"Changing Variables within a function","109":"Create and Print Tuples","1010":"Using Tuples","1011":"Tuple Immutability", "1012":"Adding and Multiplying Tuples","1013":"Creating and using Dictionaries","1014":"Calculating Scores Example", "1015":"Print Random Integers","1016":"Run Game", "1017":"Test Data Structures", "1018":"Print Method Descriptions","1019":"Run Math module test", "1020":"Print Math module components","1021":"Test floor(), ceil(), trunc() from the math module","1022":"Print Platform information","0":"Quit"}
  while True:
    displayDictionaryMenu(menu)
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


menu = {"23":"Exceptions Tests","108":"Run older code","0":"Quit"}

funLess = FunctionsLessons()

while True:
  displayDictionaryMenu(menu)
  menuChoice = getMenuChoice()
  if menuChoice == 0:
    break
  elif menuChoice == 108:
    runOlderClassWork()
  elif menuChoice == 23:
    print("\n" * 3)
    exceptionsTests()
    print("\n" * 3)