import random # importing module
import math # importing module
# from math import sin, pi # not used because of the local definition
from math import e, pi as PI # importing specific value/method
from math import sin as Sine, cos as Cosine # alias
from math import ceil, floor, trunc
from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple
from .Chess import ChessGame
from .exceptions.Test1 import NoErrorHandling
from .exceptions.Test2 import DivisionByZeroException
from .exceptions.Test3 import IndexOutOfRange
from .exceptions.Test4 import UsingIfElseToHandleDataInput
from .exceptions.Test5 import UsingTryExceptToHandleZeroDivision
from .exceptions.Test6 import ShowingCodeNotExecuted
from .exceptions.Test7 import MultipleExceptionsHandled
from .exceptions.Test8 import InsideErrorHandling, OutsideErrorHandling
from .exceptions.Test9 import RaisingAnError
from .exceptions.Test0 import UsingAssert

def exceptionsTests():
  NoErrorHandling()

  DivisionByZeroException(3)

  IndexOutOfRange(1)

  UsingIfElseToHandleDataInput()

  UsingTryExceptToHandleZeroDivision()
  
  ShowingCodeNotExecuted()
  
  MultipleExceptionsHandled()
  
  InsideErrorHandling()
  
  OutsideErrorHandling()
  
  RaisingAnError()
  
  UsingAssert()


def printPlatformInformation():
  print("platform() = ", platform())
  print("platform(1) = ", platform(1))
  print("platform(0, 1) = ", platform(0, 1))
  print("machine() = ", machine())
  print("processor() = ", processor())
  print("system() = ", system())
  print("version() = ", version())
  print("python_implementation() = ", python_implementation())

  print(python_version_tuple())
  for atr in python_version_tuple():
      print("attribute of python_version_tuple() = ", atr)

def listMathMethods():
  counter = 0
  print("__package__", math.__package__)
  for name in dir(math):
    print(name, end="\t\t")
    counter += 1
    if counter % 5 == 0:
      print()
  print("\nrandom module:")
  for name in dir(random):
    print(name, end="\t\t")
    counter += 1
    if counter % 5 == 0:
      print()
  print("\nChess module:")
  for name in dir(ChessGame):
    print(name, end="\t\t")
    counter += 1
    if counter % 5 == 0:
      print()
    
def ceilFloorTrunc():
  x = 1.4
  y = 2.6
  for i in range(0,11,2):
    x = round(i/10.0,1)
    y = round(x + .1, 1)
    print("FLOOR")
    print("floor(",x,")  = ", floor(x), " \tfloor(",y,") = ", floor(y), sep="")
    print("floor(",-x,") = ", floor(-x), " \tfloor(",-y,") = ", floor(-y), sep="")
    print("CEIL")
    print("ceil(",x,")   = ", ceil(x), " \tceil(",y,") = ", ceil(y), sep="")
    print("ceil(",-x,")  = ", ceil(-x), " \tceil(",-y,") = ", ceil(-y), sep="")
    print("TRUNC")
    print("trunc(",x,")  = ", trunc(x), " \ttrunc(",y,") = ", trunc(y), sep="")
    print("trunc(",-x,") = ", trunc(-x), " \ttrunc(",-y,") = ", trunc(-y), sep="")


def runMathTest():
  # print("sin(pi/2) =",sin(pi/2)) # using local method and throws an exception
  def sin(x):
      if 2 * x == pi:
          return 0.99999999
      else:
          return None

  pi = 3.14 # 22/7

  print("sin(pi/2) =",sin(pi/2)) # using local method
  print("sin(pi) =", sin(pi)) # should get None
  print("Sine(math.pi/2)     =", Sine(PI/2))
  print("math.sin(math.pi/2) =", math.sin(math.pi/2))
  print("math.sin(math.pi) =", math.sin(math.pi))
  print("math.sin(2 * math.pi) =", math.sin(2 * math.pi))
  print("math.sin(360) =", math.sin(360))
  print("math.sin(3.14) =", math.sin(3.14))
  print("math.sin(6.28) =", math.sin(6.28))
  print("math.sin(22/7) =", math.sin(22/7))
  print("math.sin(44/7) =", math.sin(44/7))
  print("e =", e) # using the specific value
  print("pi =", pi) # user defined pi = 3.14
  print("PI      =", PI)
  print("math.pi =", math.pi)
  print("Cosine(0) = ", Cosine(0)) # using the alias


def newFunction():
  print("new Function")

def myGlobalVariableTest():
      global var
      var = 2
      print("Do I know that variable?", var)

def displayDictionaryMenu(menuDictionary, title=""):
  menuTitle = "*** " + title + " MENU ***"
  stars = "*" * len(menuTitle)
  print("\n"+stars)
  print(menuTitle)
  print(stars)
  for key in menuDictionary:
    print("\t", end="")
    print(key, menuDictionary[key], sep=". ")
  print(stars)

def getMenuChoice(inputMessage="Please select a menu option: "):
  try:
    return int(input(inputMessage))
  except:
    print("That was an invalid entry. Please try again.")
    return getMenuChoice()

def printSetDescription():
  print("Set Description:")
  MethodsList = """
  Method\tDescription
  add()\tAdds an element to the set
  clear()\tRemoves all the elements from the set
  copy()\tReturns a copy of the set
  difference()\tReturns a set containing the difference between two or more sets
  difference_update()\tRemoves the items in this set that are also included in another, specified set
  discard()\tRemove the specified item
  intersection()\tReturns a set, that is the intersection of two other sets
  intersection_update()\tRemoves the items in this set that are not present in other, specified set(s)
  isdisjoint()\tReturns whether two sets have a intersection or not
  issubset()\tReturns whether another set contains this set or not
  issuperset()\tReturns whether this set contains another set or not
  pop()\tRemoves an element from the set
  remove()\tRemoves the specified element
  symmetric_difference()\tReturns a set with the symmetric differences of two sets
  symmetric_difference_update()\tinserts the symmetric differences from this set and another
  union()\tReturn a set containing the union of sets
  update()\tUpdate the set with the union of this set and others"""
  print(MethodsList)
  
def printDictionaryDescription():
  print("Dictionary Description:")
  MethodsList = """
  Method\tDescription
  clear()\tRemoves all the elements from the dictionary
  copy()\tReturns a copy of the dictionary
  fromkeys()\tReturns a dictionary with the specified keys and value
  get()\tReturns the value of the specified key
  items()\tReturns a list containing a tuple for each key value pair
  keys()\tReturns a list containing the dictionary's keys
  pop()\tRemoves the element with the specified key
  popitem()\tRemoves the last inserted key-value pair
  setdefault()\tReturns the value of the specified key. If the key does not exist: insert the key, with the specified value
  update()\tUpdates the dictionary with the specified key-value pairs
  values()\tReturns a list of all the values in the dictionary
  """
  print(MethodsList)

def printListDescription():
  print("List Description:") 
  MethodsList = """
  Method\tDescription
  append()\tAdds an element at the end of the list
  clear()\tRemoves all the elements from the list
  copy()\tReturns a copy of the list
  count()\tReturns the number of elements with the specified value
  extend()\tAdd the elements of a list (or any iterable), to the end of the current list
  index()\tReturns the index of the first element with the specified value
  insert()\tAdds an element at the specified position
  pop()\tRemoves the element at the specified position
  remove()\tRemoves the first item with the specified value
  reverse()\tReverses the order of the list
  sort()\tSorts the list
  """
  print(MethodsList)

def printTupleDescription():
  print("Tuple Description:")
  MethodsList = """
  Method\tDescription
  count()\tReturns the number of times a specified value occurs in a tuple
  index()\tSearches the tuple for a specified value and returns the position of where it was found
  """
  print(MethodsList)

def printRandomIntegers(maxInteger, numberOfTests):
  # print(random.random())
  # randomSingleDigit = int(random.random()*10)
  # print(randomSingleDigit)
  # randomDoubleDigit = int(random.random()*100)
  # print(randomDoubleDigit)
  for i in range(numberOfTests):
    if i%10 == 0:
      print()
    print(random.randint(1,maxInteger), end="\t")

def runGame():
  # need 6 dice
  # any number of users
  # goal of 10,000 pts
  # minimum start score = 500
  # scoring rolls
  # 1 = 100
  # 5 = 50
  # 3 of a kind = 100 * value on dice except for 1 = 1000
  # 4 of a kind = 1000
  # 5 of a kind = 2000
  # 6 of a kind = 3000
  # full house = 1500
  # straight = 1500
  # three pairs = 1500
  # two triplets = 2500
  # four of a kind with a pair = 1500
  # have to remove at least one die for each roll
  # user can stop
  # Farkle is a non-scoring roll
  # have fun
  # Farkle

  # # objects
  # score class
  #   add
  #   subtract
  #   check if roll has score

  # user class
  #   attributes: name, rank
  #   set score
  #   get score
  #   use the score class
    
  # dicecontainer class
  #   attribute number of dice = 6
  #   remove dice class
  #   score class

  # dice class
  #   attributes: number of sides = 6
  #   roll

  # menu class

  # game class
  #   list of users
  #   use the menu class
  #   use the dice class
  #   dicecontainer

  from Game.Dice import Dice

  dice1 = Dice()
  for i in range(20):
    if i % 5 == 0:
      print()
    print(" ", dice1.roll(), end=" ")
    
  print()



def printDataStructure(title, obj):
    print("\t",title, obj)
    try:
        for k,v in obj.items():
            print('\t\t>', k, ':', obj[v])
    except:
        for element in obj:
            print('\t\t>', element)

def runDataStructures():  
  newSet0 = set()
  newSet1 = set('a')
  newSet2 = {'a','b','c','d','e','f','g','h','i','j'}
  newSet3 = {1,2,3,4,5,6,7,8,9,0}
  newSet4 = {1, 'a,', 2, 'b', 3, 'c', 5.1, 7.8, 5, 6}
  
  newDic1 = {}
  newDic2 = dict()
  newDic3 = {'a':'apple','b':'banana','c':'carrot','a':'avocado'} # the second 'a' replaces the first 'a'

  newLis1 = []
  newLis2 = list()
  newLis3 = [1,2,3]

  newTup1 = ()
  newTup2 = tuple()
  newTup3 = (1,2,3)

  print("LENGTH:",len(newSet3))
  newSet3 = {1,2,3,4,5,6,7,8,9,0,0,0,0,0,0,0,0,0}
  print("LENGTH:",len(newSet3))

  print("Set:")
  printDataStructure("newSet0:", newSet0)
  printDataStructure("newSet1:", newSet1)
  printDataStructure("newSet2:", newSet2)
  printDataStructure("newSet3:", newSet3)
  printDataStructure("newSet4:", newSet4)
  print("Dictionary:")
  printDataStructure("newDic1:", newDic1)
  printDataStructure("newDic2:", newDic2)
  printDataStructure("newDic3:", newDic3)

  print("List:")
  printDataStructure("newLis1:", newLis1)
  printDataStructure("newLis2:", newLis2)
  printDataStructure("newLis3:", newLis3)
  print("Tuple:")
  printDataStructure("newTup1:", newTup1)
  printDataStructure("newTup2:", newTup2)
  printDataStructure("newTup3:", newTup3)

def printDescriptions():
  printSetDescription()
  printDictionaryDescription()
  printListDescription()
  printTupleDescription()


# def myGlobalVariableTest():
#       global var
#       var = 2
#       print("Do I know that variable?", var)

# def displayDictionaryMenu(menuDictionary):
#   for key in menuDictionary:
#     print(key, menuDictionary[key], sep=". ")

# def getMenuChoice():
#   try:
#     return int(input("Please select a menu option: "))
#   except:
#     print("That was an invalid entry. Please try again.")
#     return getMenuChoice()
