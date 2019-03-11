# Created by Ninja Hydra
import math

print("  _   _ ___ _   _     _   _ ")
print(" | \ | |_ _| \ | |   | | / \ ")
print(" |  \| || ||  \| |_  | |/ _ \ ")
print(" | |\  || || |\  | |_| / ___ \ ")
print(" |_| \_|___|_| \_|\___/_/   \_\ ")
print()
print("choose operator")
print("  'add' for addition")
print("  'sub' for subtraction")
print("  'dev' for devision")
print("  'mul' for multiplication")
print("  'sqr' for squaring ")
print("  'sqrt' for square root")
print("  'sin' for SinØ ")
print("  'cos' for CosØ ")
print("  'ln' for ln(x) ")
print("  'tan' for TanØ ")
print("  'log' for simple log(x) ")
op = input(">>> ")
if op == "add":
   num1 = float(input("Enter first number : "))
   num2 = float(input("Enter second number : "))
   result = str(num1 + num2)
   print("Result obtained is: " +result)
elif op == "sub":
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    result = str(num1 -  num2)
    print("Result obtained is :" +result)
elif op == "sqr":
    num = float(input("Enter your number : "))
    result = str(num * num)
    print("Result obtained is :" +result)
elif op == "dev":
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    result = str(num1 / num2)
    print("Result obtained is :" +result)
elif op == "mul" :
    num1 = float(input("Enter first number : " ))
    num2 = float(input("Enter second number :" ))
    result = str( num1 * num2 )
    print("Result obtained is : " +result)
elif op == "sqrt":
     from math import sqrt
     num = float(input("Enter your number: "))
     result = str(sqrt(num))
     print("Result obtained is : " +result)
elif op == "sin" :
     from math import sin 
     num = float(input("Enter Ø in radian : "))
     result = str(sin(num))
     print("Result obtained is : " +result)
elif op == "cos" :
     from math import cos 
     num = float(input("Enter Ø in radian : "))
     result = str(cos(num))
     print("Result obtained is : " +result)
elif op == "ln" :
     from math import log 
     num = float(input("Enter value of x : "))
     result = str(log(num))
     print("Result obtained is : " +result)
elif op == "log" :
     from math import log 
     num = float(input("Enter value of x : "))
     result = str( log(num) / log(10) )
     print("Result obtained is : " +result)
elif op == "tan" :
     from math import sin, cos 
     num = float(input("Enter value of Ø : "))
     result = str(sin(num) / cos(num) )
     print("Result obtained is : " +result)
else:
    print("invalid operator!!")
