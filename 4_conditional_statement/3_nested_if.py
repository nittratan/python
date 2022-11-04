# nested if statement in python
# nested if statement is used to check the condition
# if the condition is true then it will execute the statement
# if the condition is false then it will not execute the statement
# syntax
# if condition:
#     statement
#     if condition:
#         statement
#     else:
#         statement
# else:
#     statement

# check the number is positive with even or odd and negative
num=int(input("Enter a number: "))
if num>0:
    print(num,"is positive")
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
else:
    print(num,"is negative")
    