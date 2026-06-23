num1 =input("num1")
num2 =input("num2") 
num3 =input("num3")
num1= int(num1)
num2= int(num2)
num3= int(num3)

operator= input("choose +,-,*,/:")

if "operator" == "+":
    print(num1+num2+num3)
elif operator == "-":
    print(num1-num2-num3)
elif operator == "*":
    print(num1*num2*num3)
elif operator == "/":
    print(num1/num2/num3)
else:
    print("invalid operator")