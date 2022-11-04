# elif in python

# syntax
# if expression 1:
        # block of statements
# elif
        # block of statements
# elif
        # block of statements
# else
        # block of statements

# python program print weekday name using if elif else
# input from user
num = int(input("Enter a number (1-7): "))
# check condition
if num == 1:
        print("Sunday")
elif num == 2:
        print("Monday")
elif num == 3:
        print("Tuesday")
elif num == 4:
        print("Wednesday")
elif num == 5:
        print("Thursday")
elif num == 6:
        print("Friday")
elif num == 7:
        print("Saturday")
else:
        print("Invalid input! Please enter number between 1-7")