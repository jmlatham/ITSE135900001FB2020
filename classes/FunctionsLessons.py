class FunctionsLessons:
  def __init__(self):
    pass

  def __printSpaces__(self):
    print("\n"*3)
  
  def __printLineSeparator__(self):
    print("--------------------------")

  def printMyTupleContents(self, tupleToPrint, message="My Tuple's Contents:"):
    print(message, tupleToPrint)
  
  def calculatingScoresExample(self):
    self.__printLineSeparator__()
    school_class = {}

    while True:
        name = input("Enter the student's name (or type exit to stop): ")
        if name == 'exit':
            break
        
        score = int(input("Enter the student's score (0-10): "))
        
        if name in school_class:
            school_class[name] += (score,)
        else:
            school_class[name] = (score,)
            
    for name in sorted(school_class.keys()):
        print("tuple: ", school_class[name])
        adding = 0
        counter = 0
        for score in school_class[name]:
            adding += score
            counter += 1
        print(name, ":", adding / counter)
    
    self.__printSpaces__() 
  
  def createAndPrintTuples(self):
    self.__printLineSeparator__()
    print("\ntuple1 = (1, 2, 4, 8)  #<--- create a tuple")
    tuple1 = (1, 2, 4, 8)
    self.printMyTupleContents(tuple1, "\tContents: ")
    print("\ntuple2 = 1., .5, .25, .125  #<--- another way to create a tuple")
    tuple2 = 1., .5, .25, .125
    self.printMyTupleContents(tuple2, "\tContents: ")
    print("\noneElementTuple1 = (1, )  #<--- one way to create a one element tuple")
    oneElementTuple1 = (1, )
    self.printMyTupleContents(oneElementTuple1, "\tContents: ")
    print("\noneElementTuple2 = 1.,   #<--- another way to create a one element tuple")
    oneElementTuple2 = 1., 
    self.printMyTupleContents(oneElementTuple2, "\tContents: ")
    print("\noneElementTuple3 = 1.  #<--- this is not a tuple")
    oneElementTuple3 = 1.
    self.printMyTupleContents(oneElementTuple3, "\tContents: ")
    print("\nNotice the difference between tuple and float")
    self.printMyTupleContents(oneElementTuple2, "\tContents: ")
    self.printMyTupleContents(oneElementTuple3, "\tContents: ")
    self.__printSpaces__() 

  def usingTuples(self):
    self.__printLineSeparator__()
    print("myTuple = (1, 10, 100, 1000, 'a','b','c')")
    myTuple = (1, 10, 100, 1000, 'a','b','c')
    self.printMyTupleContents(myTuple,"\t")

    print("myTuple[0]")
    self.printMyTupleContents(myTuple[0],"\t")
    print("myTuple[-1]")
    self.printMyTupleContents(myTuple[-1],"\t")
    print("myTuple[1:]")
    self.printMyTupleContents(myTuple[1:],"\t")
    print("myTuple[:-2]")
    self.printMyTupleContents(myTuple[:-2],"\t")

    for elem in myTuple:
        print(elem)

    self.__printSpaces__() 

  def appendToObject(self, obj, valueToAppend, message="Cannot append."):
    try:
      print("Excecute Append function.")
      obj.append(valueToAppend)
      print(obj)
      return obj
    except:
      print(message)

  def tupleImmutability(self):
    self.__printLineSeparator__()
    print("myTuple = () -- this produces an empty Tuple")
    myTuple = ()
    self.printMyTupleContents(myTuple)
    print("call appendToObject")
    self.appendToObject(myTuple, 1)
    print("value of the appendToObject method")
    print(self.appendToObject(myTuple, 1))
    print()
    print()
    # try:
    #   print("Execute myTuple.append(1):")
    #   myTuple.append(1)
    # except:
    #   print("\tCannot append to a Tuple")
    print("\nmyTuple = ('a','b','c') -- this creates a new Tuple with data")
    myTuple = ('a','b','c')
    self.printMyTupleContents(myTuple)
    print(self.appendToObject(myTuple, 'd'))
    print()
    print(myTuple[0])
    try:
      myTuple[0] = "z"
    except:
      print("TypeError: 'tuple' object does not support item assignment")
    # try:
    #   print("Execute myTuple.append('d'):")
    #   myTuple.append('d')
    # except:
    #   print("\tStill cannot append to a Tuple")
    myList = [1,2,3]
    print(self.appendToObject(myList, 4))
    self.__printSpaces__()

  def addingAndMultiplyingTuples(self):
    self.__printLineSeparator__()
    print("myTuple = (1, 10, 100) #<--- this creates a tuple")
    myTuple = (1, 10, 100)
    self.printMyTupleContents(myTuple, "\t")
    print("t1 = myTuple + (1000, 10000) #<--- this creates a new tuple")
    t1 = myTuple + (1000, 10000)
    self.printMyTupleContents(t1, "\t")
    print("t2 = myTuple * 3 #<--- this creates a new tuple")
    t2 = myTuple * 3
    self.printMyTupleContents(t2, "\t")

    print("len(t2) =", end=" ")
    print(len(t2))
    # print(t1)
    # print(t2)
    print("Is 10 in myTuple? ", end="")
    print(10 in myTuple)
    if 10 in myTuple:
      print("YAAAAAY")
    print("\t 10 in myTuple")
    print("Is -10 not in myTuple? ", end="")
    print(-10 not in myTuple)
    if -10 not in myTuple:
      print("BOOOOO")
    print("\t -10 not in myTuple")
    self.__printSpaces__()

  def creatingDictionaries(self):
    self.__printLineSeparator__()

    print('create dictionary:\n\tdictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}')

    dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

    printMessage = """\nloop through the keys in the dictionary:
\tfor key in dictionary.keys():
\t\tprint(key, "->", dictionary[key]) \n"""
    print(printMessage)

    for key in dictionary.keys():
        print(key, "->", dictionary[key])

    printMessage = """\nloop through the items in the dictionary:
\tfor english, french in dictionary.items():
\t\tprint(english, "->", french) \n"""
    print(printMessage)

    for english, french in dictionary.items():
        print(english, "->", french)

    printMessage = """\nloop through the values in the dictionary:
\tfor french in dictionary.values():
\t\tprint(french) \n"""
    print(printMessage)

    for french in dictionary.values():
        print(french)

    print()
    print("To change a value: dictionary['cat'] = 'minou'")
    print("To add a new key:value pair: dictionary['swan'] = 'cygne'")
    print() 
    print(dictionary, " # <--- original values")
    dictionary['cat'] = 'minou'
    print(dictionary, " # <--- cat value is changed")
    dictionary['swan'] = 'cygne'
    print(dictionary, " # <--- swan value is added")

    self.__printSpaces__()








  def makingFunctions(self):
    self.__printLineSeparator__()

    def printMessage():
      print("Please enter a value: ")

    def getIntValue(message= "Please enter an integer value: "):
      # message = "Please enter an integer value: "
      try:
        return int(input(message))
      except:
        print("That value was not an integer.")
        return getIntValue()

    # print("Enter a value:")
    # a = int(input())
    # print("Enter a value:")
    # b = int(input())
    # print("Enter a value:")
    # c = int(input())
    # print("a =", a, "\nb =", b, "\nc =", c)
    
    # printMessage()
    # d = int(input())
    # printMessage()
    # e = int(input())
    # printMessage()
    # f = int(input())
    # print("\n\nd =", d, "\ne =", e, "\nf =", f)

    g = getIntValue()
    h = getIntValue("Please enter a second integer value: ")
    i = getIntValue("One more time: ")
    print("\n\ng =", g, "\nh =", h, "\ni =", i)

    self.__printSpaces__()

  def positionalKeywordArguments(self):
    self.__printLineSeparator__()
    def addingTest(a, b, c):
      print(a, "+", b, "+", c, "=", a + b + c)

    addingTest(1,2,3)
    addingTest(3,2,1)
    addingTest(1,2,c=3)
    addingTest(1,b=2,c=3)
    addingTest(1,c=2,b=3)
    addingTest(a=1,b=2,c=3)
    # addingTest(a=1,2,c=3)
    # addingTest(1,a=2,c=3)

    self.__printSpaces__()

  def usingNone(self):
    self.__printLineSeparator__()

    def testFunction(value):
      if value == 0:
          return
      else:
          return value

    print(testFunction(0))

    if testFunction(0) == None:
        print("testFunction() returned None --> ", testFunction(0))
    else:
        print("testFunction() returned another value --> ", testFunction(0))
        
    print(testFunction(1))

    if testFunction(1) == None:
        print("testFunction() returned None --> ", testFunction(1))
    else:
        print("testFunction() returned another value --> ", testFunction(1))

    self.__printSpaces__()

  def strangeFunction(self):
    self.__printLineSeparator__()

    def numberIsEven(n):
      if(n % 2 == 0):
          return True

    [print("number is even: ",numberIsEven(x)) for x in range(5)]

    self.__printSpaces__()

  def showScope(self):
    self.__printLineSeparator__()
    def scopeTest1():
      x = 123

    def scopeTest2():
      print(y)

    def scopeTest3():
      # print("z inside =", z)
      z = 5 # this causes the error on line 97! - show the difference
      print("z inside =", z)

    scopeTest1()
    try:
        print(x)
    except:
        print("Error: x is not defined")
    y="yes"
    scopeTest2()
    z = 3
    print("z outside =",z)
    scopeTest3()
    print("z outside =",z)

    self.__printSpaces__()

  def keywordGlobal(self):
    # with the nested functions, the global keyword is not working correctly
    # look at the code in main.py
    self.__printLineSeparator__()
    def myFunction():
      global var
      var = 2
      print("Do I know that variable?", var)

    var = 1
    print("before calling myFunction():", var)
    myFunction()
    print("after calling myFunction():", var)

    self.__printSpaces__()

  def changeVariableWithinFunction(self):
    self.__printLineSeparator__()
    
    def myFunction1(n):
      print("I got", n)
      n += 1
      print("I have", n)

    var = 1
    myFunction1(var)
    print(var)

    def myFunction2(myList1):
        print("inside function:")
        print(myList1)
        myList1 = [0, 1] # uses the passed list until changed - show the difference
        print(myList1)
        del myList1[0]
        print(myList1)

    myList2 = [2, 3]
    myFunction2(myList2)
    print("outside of function:")
    print(myList2)

    self.__printSpaces__()




# # Special code:
# def myfunc(**kwargs):
#     # kwargs is a dictionary.
#     for k,v in kwargs.iteritems():
#          print "%s = %s" % (k, v)

# myfunc(abc=123, efh=456)
# # abc = 123
# # efh = 456
# And you can mix the two:

# def myfunc2(*args, **kwargs):
#    for a in args:
#        print a
#    for k,v in kwargs.iteritems():
#        print "%s = %s" % (k, v)

# myfunc2(1, 2, 3, banan=123)
# # 1
# # 2
# # 3
# # banan = 123