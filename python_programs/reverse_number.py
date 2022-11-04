# reverse a number using while loop
# input from user
num = int(input("Enter a number: "))
rev = 0
while num > 0:
        # logic
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10

print("Reverse of the number is:",rev)