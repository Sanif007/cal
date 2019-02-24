# Created by Ninja Hydra

print("  _   _ ___ _   _     _   _ ")
print(" | \ | |_ _| \ | |   | | / \ ")
print(" |  \| || ||  \| |_  | |/ _ \ ")
print(" | |\  || || |\  | |_| / ___ \ ")
print(" |_| \_|___|_| \_|\___/_/   \_\ ")
print("choose operator")
print("  'add' for addition")
print("  'sub' for subtraction")
print("  'dev' for devision")
print("  'mul' for multiplication")
print("  'sqr' for squaring ")
print("  'sqrt' for square root")
op = input(">>> ")
if op == "add":
   num1 = float(input("Enter first number : "))
   num2 = float(input("Enter second number : "))
   #Extra space in line 13 and 14.
   result2 = str(num1 + num2)
   print("Result obtained is: " +result2)
elif op == "sub":
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    result3 = str(num1 -  num2)
    print("Result obtained is :" +result3)
elif op == "sqr":
    num = float(input("Enter your number : "))
    result4 = str(num * num)
    print("Result obtained is :" +result4)
elif op == "dev":
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    #Wrong division sign was used.
    result5 = str(num1 / num2)
    print("Result obtained is :" +result5)
elif op == "mul" :
    num1 = float(input("Enter first number : " ))
    num2 = float(input("Enter second number :" ))
    result6 = str( num1 * num2 )
    print("Result obtained is : " +result6)
elif op == "sqrt":
     from math import sqrt
     num = float(input("Enter your number: "))
     result7 = str(sqrt(num))
     print("Result obtained is : " +result7)
else:
    print("invalid operator!!")
    