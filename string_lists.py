# Exercise:
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
#Example of palindrome:
# phrase = "acrobatsstaborca"

phrase = input('Enter a string: ').lower()


if phrase[:] == phrase[::-1]:
    print("This string is a palindrome")





