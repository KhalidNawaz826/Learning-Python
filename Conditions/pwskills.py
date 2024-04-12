num = int(input("Enter a number:"))
if (num > 5):
    print("The number is greater than 5.")
elif num == 5:
    print("The number is equal to 5.")
else:
    print("The number is less than 5.")

#Grading System
marks = int(input("Enter your marks:"))
if marks >= 90:
    print("Grade A+")
elif marks >=80 :
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")

#Ternary Operators
num = int(input("Enter a number:"))
result = "EVEN" if num %2 == 0 else "ODD"
print("The number is ", result)

#Match and case statements
day_num = int(input("Enter a number to display a day accordingly:"))
match day_num:
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is wednesday")
    case 4:
        print("Today is Thursday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Invalid input")