Erste_Nummer = float(input('bitte reichen sie deine erste Nummer ein : '))
Zweite_Nummer = float(input('bitte reichen sie andere nummer ein : '))
Operator = input('welche funktion soll dazwischen gemacht werden(+or-or/or*): ')

if Operator == '+' :
    result = Erste_Nummer+Zweite_Nummer
elif Operator == '-' :
    result = Erste_Nummer-Zweite_Nummer
elif Operator == '/' :
    if Zweite_Nummer == 0 :
        result = 'mathematisch ist es leider nicht Möglich'
    else:
        result = Erste_Nummer/Zweite_Nummer
elif Operator == '*' :
   result = Erste_Nummer*Zweite_Nummer 
else:
   result = "unvefügbare Operation"

print(result)