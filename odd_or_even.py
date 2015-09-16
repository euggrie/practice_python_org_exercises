# Exercise:
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
# to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Enter a number: "))
check = int(input("Enter another number: "))


if number % 2 == 0 and number % 4 ==0:
    print("{} is an even number and is a multiple of 4.".format(number))
elif number % 2 == 0:
    print("{} is an even number.".format(number))
else:
    print("{} is an odd number.".format(number))


if number % check == 0:
    print("{} is divisible by {}.".format(number, check))
else:
    print("{} is not divisible by {}.".format(number, check))


