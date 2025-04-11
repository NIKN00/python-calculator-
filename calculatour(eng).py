First_Number = float(input('Please insert your First Number : '))
Second_Number = float(input('Please insert your second Number : '))
Operator = input('what kind of opreations should be done(+or-or/or*): ')

if Operator == '+' :
    result = First_Number+Second_Number
elif Operator == '-' :
    result = First_Number-Second_Number
elif Operator == '/' :
    if Second_Number == 0 :
        result = 'mathematica it is not Possible'
    else:
        result = First_Number/Second_Number
elif Operator == '*' :
   result = First_Number*Second_Number 
else:
   result = "unreachable Operation"

print(result)