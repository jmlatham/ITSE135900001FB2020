from .functions import displayDictionaryMenu, getMenuChoice

class Labs5:
  def __init__(self):
    pass
  
  def printLab5_1_6_4(self):
    print("Estimated time: 15-25 minutes")
    print("Level of difficulty: Medium")
    print("Objectives: improving the student's skills in defining functions; using exceptions in order to provide a safe input environment.")
    print("Scenario: Your task is to write a function able to input integer values and to check if they are within a specified range.")
    print("The function should:")
    print("\taccept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;")
    print("\tif the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;")
    print("\tif the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;")
    print("\tif the input value is valid, return it as a result.")
    print("Test data")
    print("Test your code carefully.")
    print("\nThis is how the function should react to the user's input:")
    print("""Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1""")

  def lab5_1_6_4(self):
    runMenu = {"0":"Quit","1":"Run Lab 5.1.6.4","2":"Print Instructions"}
    
    while True:
      displayDictionaryMenu(runMenu, "Lab 5.1.6.4")
      menuChoice = getMenuChoice()
      if menuChoice == 0:
        break
      elif menuChoice == 2:
        self.printLab5_1_6_4()
      else:
        self.runLab5_1_6_4()

  
  def runLab5_1_6_4(self):
    def readint(prompt, min, max):
      try:
        integerValue = int(input(prompt))
        if integerValue < min or integerValue > max:
          print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
          readint(prompt, min, max)
        else:
            return integerValue
      except:
        print("Error: wrong input.")
        readint(prompt, min, max)

    v = readint("Enter a number from -10 to 10: ", -10, 10)

    print("The number is:", v)

  def printLab5_1_9_18(self):
    print("")
    print("Estimated time: 20-25 minutes")

    print("Level of difficulty: Medium")

    print("Objectives: improving the student's skills in operating with strings; using built-in Python string methods.")
    print("""Scenario:
\tYou already know how split() works. Now we want you to prove it.

\tYour task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

\tit should accept exactly one argument - a string;
\tit should return a list of words created from the string, divided in the places where the string contains whitespaces;
\tif the string is empty, the function should return an empty list;
\tits name should be mysplit()
\tUse the template in the editor. Test your code carefully.

Expected output:
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
[]
['abc']
[]""")

  def lab5_1_9_18(self):
    runMenu = {"0":"Quit","1":"Run Lab 5.1.9.18","2":"Print Instructions"}
    
    while True:
      displayDictionaryMenu(runMenu, "Lab 5.1.9.18")
      menuChoice = getMenuChoice()
      if menuChoice == 0:
        break
      elif menuChoice == 2:
        self.printLab5_1_9_18()
      else:
        self.runLab5_1_9_18()
  def runLab5_1_9_18(self):
    def mysplit(strng):
      stringList = []
      tempString = ""
      for char in strng:
        if(char != " "):
          tempString += char
        else:
          if len(tempString) > 0:
            stringList.append(tempString)
          tempString = ""
      return stringList
    print("\nmysplit('To be or not to be, that is the question')")
    print(mysplit("To be or not to be, that is the question"))
    print('\nmysplit("To be or not to be,that is the question")')
    print(mysplit("To be or not to be,that is the question"))
    print('\nmysplit("   ")')
    print(mysplit("   "))
    print('\nmysplit(" abc ")')
    print(mysplit(" abc "))
    print('\nmysplit("")')
    print(mysplit(""))

  def printLab5_1_10_6(self):
    print("instructions")
    print("""
Estimated time: 30 minutes

Level of difficulty: Medium

Objectives: improving the student's skills in operating with strings; using strings to represent non-text data.
Scenario:
\tYou've surely seen a seven-segment display.

\tIt's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

\tYour task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

\tEach digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.

Test data
Sample input:

123

Sample output:

  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

Sample input:

9081726354

Sample output:

### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 
""")

  def lab5_1_10_6(self):
    runMenu = {"0":"Quit","1":"Run Lab 5.1.10.6","2":"Print Instructions"}
    
    while True:
      displayDictionaryMenu(runMenu, "Lab 5.1.10.6")
      menuChoice = getMenuChoice()
      if menuChoice == 0:
        break
      elif menuChoice == 2:
        self.printLab5_1_10_6()
      else:
        self.runLab5_1_10_6()
  
  def runLab5_1_10_6(self):
    zero = ['###','# #','# #','# #','###']
    one = ['  #','  #','  #','  #','  #']
    two = ['###','  #','###','#  ','###']
    three = ['###','  #','###','  #','###']
    four = ['# #','# #','###','  #','  #']
    five = ['###','#  ','###','  #','###']
    six = ['###','#  ','###','# #','###']
    seven = ['###','  #','  #','  #','  #']
    eight = ['###','# #','###','# #','###']
    nine = ['###','# #','###','  #','  #']
    space = [' ',' ',' ',' ',' ']
    def getNumberSection(number, section):
      if number == 0:
        return zero[section]
      elif number == 1:
        return one[section]
      elif number == 2:
        return two[section]
      elif number == 3:
        return three[section]
      elif number == 4:
        return four[section]
      elif number == 5:
        return five[section]
      elif number == 6:
        return six[section]
      elif number == 7:
        return seven[section]
      elif number == 8:
        return eight[section]
      elif number == 9:
        return nine[section]
      else:
        return space[section]

    def isInt(value):
      try:
        x = int(value)
        return True
      except:
        return False

    def getLEDDisplay(value):
      ledDisplay = ""
      if isInt(value):
        strValue = str(value)
        for section in range(5):
          for char in strValue:
            ledDisplay += getNumberSection(int(char), section)
            ledDisplay += getNumberSection(-1,section)
          ledDisplay += "\n"
        return ledDisplay
      else:
        return "not an integer"

    print("123\n")
    print(getLEDDisplay(123))
    print("9081726354\n")
    print(getLEDDisplay("9081726354"))

    while True:
      try:
        menuChoice = int(input("Enter a 1 if you would like to your own number: "))
        if menuChoice != 1:
          break
        else:
          print(getLEDDisplay(input("Integer: ")))
          print()
      except:
        break