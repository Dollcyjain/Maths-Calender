import calendar
import math


def cal():
    years = int(input("Enter the year for the calender: "))
    month = int(input("Enter the number of months you want in a line: "))
    print(calendar.calendar(years, 3, 1, 10, month))


def leap():
    year = int(input("Enter the year: "))
    ans = calendar.isleap(year)
    if ans == False:
        print("No!!", year, "is not a leap year")
    else:
        print("Yes!!", year, "is a leap year")


def mathop():
    operations = ["Addition", "Subtraction", "Division", "Multiplication", "Factorial", "Logarithm", "Square root",
                  "Convert radians to degrees"]
    print("This calculator do operations listed below.\nYou can choose one option")
    i = 0
    for operations[i] in operations:
        print(str(i + 1) + ".", operations[i])
        i += 1
    op = int(input())
    if op == 1:
        opr1 = int(input("Enter number1: "))
        opr2 = int(input("Enter number2: "))
        result = opr1 + opr2
        print("result =", result)
    elif op == 2:
        opr1 = int(input("Enter number1: "))
        opr2 = int(input("Enter number2: "))
        result = opr1 - opr2
        print("result =", result)
    elif op == 3:
        opr1 = int(input("Enter number1: "))
        opr2 = int(input("Enter number2: "))
        result = opr1 / opr2
        print("result =", result)
    elif op == 4:
        opr1 = int(input("Enter number1: "))
        opr2 = int(input("Enter number2: "))
        result = opr1 * opr2
        print("result =", result)
    elif op == 5:
        opr1 = int(input("Enter number: "))
        result = math.factorial(opr1)
        print("result =", result)
    elif op == 6:
        opr1 = int(input("Enter number: "))
        opr2 = int(input("Enter base: "))
        result = math.log(opr1, opr2)
        print("result =", result)
    elif op == 7:
        opr1 = int(input("Enter number: "))
        result = math.sqrt(opr1)
        print("result =", result)
    elif op == 8:
        opr1 = int(input("Enter number: "))
        result = math.degrees(opr1)
        print("result =", result)
    else:
        print("Option Not Available!!")


print("In which section you want to go?\n1. Calender\n2. Math")
sec = int(input())
if sec == 1:
    print("*** Welcome to Calendar Section ***")
    print("What you want to do?\n1. See Calender\n2. Check year is leap or not")
    try:
        # jhsdasuy
        act = int(input())
        if act == 1:
            cal()
        elif act == 2:
            leap()
        else:
            print("Option Not Available!!")
    except:
        print("Invalid input\n")
elif sec == 2:
    print("*** Welcome to Math Section ***")
    mathop()
else:
    print("Option Not Available")
