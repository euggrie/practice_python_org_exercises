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


