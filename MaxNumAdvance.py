num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

Max = num1

if num2 > Max:
    Max = num2
    if num3 > Max:
        Max = num3
        print("The maximum number is", Max)
    else:
        print("The maximum number is", Max)
elif num3 > Max:
    Max = num3
    print("The maximum number is", Max)
else:
    print("The maximum number is", Max)