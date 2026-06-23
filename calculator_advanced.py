import math

while True:
    print("Welcome to advanced calculator, choose an operator")
    print("1. Add(+)") 
    print("2. Subtract(-)") 
    print("3. Multiply(*)") 
    print("4. Divide(/)") 
    print("5. Square root(√)") 
    print("6. Power(^)") 
    print("7. Modulus(%)")
    print("8. Quit")

    operator = input("Enter your choice (1-8): ")

    if operator == "1":
        try:
            num1= int(input("num1: "))
            num2= int(input("num2: "))
            num3= int(input("num3: "))
            print(num1+num2+num3)
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif operator == "2":
        try:
            num1= int(input("num1: "))
            num2= int(input("num2: "))
            num3= int(input("num3: "))
            print(num1-num2-num3)
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif operator == "3":
        try:
            num1= int(input("num1: "))
            num2= int(input("num2: "))
            num3= int(input("num3: "))
            print(num1*num2*num3)
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif operator == "4":
        try:
            num1= int(input("num1: "))
            num2= int(input("num2: "))
            num3= int(input("num3: "))
            print(num1/num2/num3)
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif operator == "5":
        try:
            num1= int(input("num1: "))
            print(math.sqrt(num1))
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif operator == "6":
        try:
            num1= int(input("num1: "))
            num2= int(input("num2: "))
            print(num1**num2)
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif operator == "7":
        try:
            num1= int(input("num1: "))
            num2= int(input("num2: "))
            print(num1%num2)
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif operator == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please choose 1-8")

