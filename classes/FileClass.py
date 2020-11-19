# import sys
# sys.path.append("../files/")
# filesPath = "../files/"
from os import strerror

class FileClass:
  __filesPath = "files/"
  __fileName = "tzop.txt"
  __file = __filesPath + __fileName
  def __init__(self):
    pass

  def readFirstFile(self):  
    stream = open(self.__file, "rt", encoding = "utf-8") # opening tzop.txt in read mode, returning it as a file object
    print(stream.read()) # printing the content of the file

  def readSecondFile(self):
    try:
      cnt = 0
      # s = open('text.txt', "rt")
      s = open(self.__file, "rt")
      ch = s.read(1)
      while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
      s.close()
      print("\n\nCharacters in file:", cnt)
    except IOError as e:
      print("I/O error occurred: ", strerror(e.errno))

  def readThirdFile(self):
    try:
      ccnt = cplncnt = lcnt = 0
      s = open(self.__file, 'rt')
      line = s.readline()
      while line != '':
        lcnt += 1
        cplncnt = 0
        for ch in line:
          if ch != "\n":
            print(ch, end='')
          else:
            print("", end='')
          ccnt += 1
          cplncnt += 1
        print(" -->", cplncnt, "characters")
        line = s.readline()
      s.close()
      print("\n\nCharacters in file:", ccnt)
      print("Lines in file:     ", lcnt)
    except IOError as e:
      print("I/O error occurred:", strerror(e.errno))

  def readLinesCode(self, separateCharacters):
    try:
      ccnt = lcnt = 0
      s = open(self.__file, 'rt')
      lines = s.readlines()
      while len(lines) != 0:
        for line in lines:
          lcnt += 1
          if separateCharacters:
            for ch in line:
              print(ch, end='-')
              ccnt += 1
          else: 
            print(line, end="")
        lines = s.readlines(10)
      s.close()
      print("\n\nCharacters in file:", ccnt)
      print("Lines in file:     ", lcnt)
    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))

  def readFile(self, fileName):
    try:
      stream = open(self.__filesPath+fileName, "rt", encoding = "utf-8") # opening tzop.txt in read mode, returning it as a file object
      print(stream.read()) # printing the content of the file
    except IOError as e:
      print("I/O error occurred:", strerror(e.errno))

  def writeFile(self):
    try:
      fo1 = open(self.__filesPath+'newtext.txt', 'w') # a new file (newtext.txt) is created
      fo2 = open(self.__filesPath+'newtext2.txt', 'a') # a new file (newtext.txt) is created
      for i in range(10):
        s = "line #" + str(i+1)
        if i<9:
          s += "\n"
        for ch in s:
          fo1.write(ch)
      for i in range(10):
        s = "line #" + str(i+11) + "\n"
        for ch in s:
          fo2.write(ch)
      fo1.close()
      fo2.close()
      self.readFile('newtext.txt')
      self.readFile('newtext2.txt')
    except IOError as e:
      print("I/O error occurred: ", strerror(e.errno))
  
  def filesAndDirectories(self):
    from os import listdir
    from os import walk
    from os.path import isfile, join

    onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
    print(onlyfiles)

    f = []
    for (dirpath, dirnames, filenames) in walk("."):
      if("__pycache__" in dirpath):
        continue
      if(".git" in dirpath):
        continue
      if ".upm" in dirpath:
        continue
      # if("__pycache__" in dirnames ):
      #   continue
      print("\n" * 2)
      print("dirpath:",dirpath)
      print("dirnames:",dirnames)
      print("filenames:", filenames)
      if dirpath == "./files":
      # if "newtext.txt" in filenames:
        for fileName in filenames:
          self.readFile(fileName)
      f.extend(filenames)
      print(f)
      # break
    # print(f)
    print("The End!")