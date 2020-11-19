from .DecimalToBinary import DecimalToBinary

class BitwiseOperator:
  def __init__(self):
    pass

  def And(self, value1, value2):
    return value1 & value2

  def Or(self, value1, value2):
    return value1 | value2
  
  def Not(self, value):
    binaryValue = DecimalToBinary(value)
    notBinaryValue = ""
    for digit in binaryValue:
      if digit == "1":
        notBinaryValue = notBinaryValue + "0"
      else:
        notBinaryValue = notBinaryValue + "1"
    return notBinaryValue
  
  def Xor(self, value1, value2):
    return value1 ^ value2
  
  def LeftShift(self, valueToShift, shiftValue):
    return valueToShift << shiftValue
  
  def RightShift(self, valueToShift, shiftValue):
    return valueToShift >> shiftValue