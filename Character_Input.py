
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
year = 2015 - age + 100
number = int(input("Choose a number: "))

for x in range(1,number):
    print("In the year {}, {} will turn 100 years old.\n".format(year, name))
