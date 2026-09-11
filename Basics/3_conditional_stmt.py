score=int(input("Enter your marks : "))

if score>=90:
    print("Grade A+")
    if score>=95:
        print("Outstanding!!!")
elif score>=80:
    print("Grade A")
elif score>=70:
    print("Grade B")
elif score>=60:
    print("Grade C")
else:
    print("fail")
    
day=int(input("Enter your day : "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
