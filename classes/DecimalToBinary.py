def DecimalToBinary(num): 
    digit = 0
    if num > 1: 
        digit = DecimalToBinary(num // 2) 
    if(str(digit)+ str(num % 2) == "01"):
      return "1"
    elif(str(digit)+str(num%2) == "00"):
      return "0"
    return str(digit) + str(num % 2) 