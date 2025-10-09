print("simple calculator")
symbol = input("enter the arithmetic operation symbol:\n")

num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

if symbol == "+":
    print(num1 + num2)
elif symbol == "-":
    print( num1 - num2)
elif symbol == "*":
    print( num1 * num2)
elif symbol == "**":
    print(num1 ** num2)
elif symbol == "%":
    print(num1 % num2)
elif symbol == "/":
    print(num1 / num2)