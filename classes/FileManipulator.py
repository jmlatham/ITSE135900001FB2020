from .functions import displayDictionaryMenu, getMenuChoice
from os import strerror
import re

class FileManipulator:
  __filesPath = "files/"
  def __init__(self):
    pass
  
  def printVerticalSpace(self, spaces=1):
    try:
      spaces = int(spaces)
    except:
      spaces = 1
    print("\n" * spaces)

  def getFileName(self):
    return input("Enter name of File: ")

  def writeToFile(self):
    print("Write to File")
    fileName = self.getFileName()
    print(fileName)
    try:
      fo = open(self.__filesPath+fileName, 'w')
      while True:
        textToWrite = input("Please enter the text to write: ")
        if(textToWrite == ""):
          break
        fo.write(textToWrite + "\n")
      # for i in range(10):
      #   s = "line #" + str(i+1) + "\n"
      #   for ch in s:
      #     fo.write(ch)
      fo.close()
      self.readFile(fileName)
    except IOError as e:
      print("I/O error occurred: ", strerror(e.errno))
  
  def readFile(self, fileName=""):
    print("Read From File")
    if fileName == "":
      fileName = self.getFileName()
    print(fileName)
    try:
      stream = open(self.__filesPath+fileName, "rt", encoding = "utf-8") # opening tzop.txt in read mode, returning it as a file object
      print(stream.read()) # printing the content of the file
    except IOError as e:
      print("I/O error occurred: ", strerror(e.errno))

  def appendToFile(self):
    print("Append To File")
    fileName = self.getFileName()
    print(fileName)
    try:
      fo = open(self.__filesPath+fileName, 'a')
      while True:
        textToWrite = input("Please enter the text to append: ")
        if(textToWrite == ""):
          break
        fo.write(textToWrite + "\n")
      # for i in range(10):
      #   s = "line #" + str(i+11) + "\n"
      #   for ch in s:
      #     fo.write(ch)
      fo.close()
      self.readFile(fileName)
    except IOError as e:
      print("I/O error occurred: ", strerror(e.errno))
  
  def getFileNameMenu(self):
    print("Display Files")
    fileDictionary = {"0":"fileTest.txt","1":"tzop.txt"}
    displayDictionaryMenu(fileDictionary, "FILE")
    return fileDictionary
  
  # def getFileId(self):
  #   try:
  #     return input("Which file do you want to search? ")
  #   except:
  #     print("Bad selection")
  #     return self.getFileId()

  def searchFile(self):
    print("Search File")
    fileNameDictionary = self.getFileNameMenu()
    fileId = str(getMenuChoice("Please select a file: "))
    searchString = input("What do you seek? ")
    try:
      print(fileNameDictionary)
      print(fileId)
      print(fileNameDictionary[fileId]) # this is trowing an error!!!
      print(searchString)
      stream = open(self.__filesPath+fileNameDictionary[fileId], "rt", encoding = "utf-8") 
      print(stream.read()) # printing the content of the file
      line = stream.readline()
      lcnt = 1
      while line != '':
        result = re.search(searchString, line)
        if result:
          print(lcnt,line, sep=" - ")
        lcnt += 1
        # cplncnt = 0
        # for ch in line:
        #   if ch != "\n":
        #     print(ch, end='')
        #   else:
        #     print("", end='')
        #   ccnt += 1
        #   cplncnt += 1
        # print(" -->", cplncnt, "characters")
        line = stream.readline()
      stream.close()
    except IOError as e:
      print("I/O error occurred: ", strerror(e.errno))
    

  def run(self):
    self.printVerticalSpace(2)
    menu = {"0":"Quit File Manipulator","1":"Write to File","2":"Read File","3":"Append to File","4":"Search File"}
    while True:
      displayDictionaryMenu(menu)
      choice = getMenuChoice()
      if choice == 0:
        break
      elif choice == 1:
        self.printVerticalSpace()
        self.writeToFile()
        self.printVerticalSpace()
      elif choice == 2:
        self.printVerticalSpace()
        self.readFile()
        self.printVerticalSpace()
      elif choice == 3:
        self.printVerticalSpace()
        self.appendToFile()
        self.printVerticalSpace()
      elif choice == 4:
        # print("\n\n<<-- THIS IS COMING SOON!! -->>\n")
        self.printVerticalSpace()
        self.searchFile()
        self.printVerticalSpace()
    self.printVerticalSpace()