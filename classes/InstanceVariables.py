class InstanceVariables:
  classCounter = 0
  counter = 0
  def __init__(self, val = 1):
    self.__first = val # private
    self.first = val
    InstanceVariables.classCounter += 1
    self.counter += 1

  def setSecond(self, val = 2):
    self.__second = val # private
    self.second = val

if __name__ == "__main__":
  exampleObject1 = InstanceVariables()
  exampleObject2 = InstanceVariables(2)

  exampleObject2.setSecond(3)

  exampleObject3 = InstanceVariables(4)
  exampleObject3.__third = 5 # not private
  exampleObject3.third = 5


  print(exampleObject1.__dict__, exampleObject1.counter, exampleObject1.classCounter)
  print(exampleObject2.__dict__, exampleObject2.counter, exampleObject2.classCounter)
  print(exampleObject3.__dict__, exampleObject3.counter, exampleObject3.classCounter)