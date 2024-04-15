# Entering variables and printing them with the "print()" function.
# Values can be integers, strings, or boolean values.
age = 20
price = 19.95
# Strings are identified with single or double quotes.
first_name = "James"
is_online = True
# You can't combine variables of different types.
# They need to be converted from one type to another.
print(first_name+" is "+str(age)+".")

# You can prompt the user for a value using the "input()" function.
# Adding a space at the end of the prompt makes the input field look better.
name = input("What is your name? ")
print("Hello "+name+"!")

# Input is always a string, so it needs to be converted for math.
birth_year = input("Enter your birth year: ")
# This can be problematic; it needs input validation.
# If I enter 90 instead of 1990, I will be very old indeed.
age2 = 2024-int(birth_year)
# Additionally, if I say I was born *after* 2024, I am younger than 0.
# I would probably want to grab current year from something...
print(name+", you are probably "+str(age2)+" year(s) old.")

# Exercise 2(I think... sometime around 14:25)
first_integer = input("Input the first number (to be subtracted from): ")
# The "float" function can also be performed at time of value retrieval.
# Maybe it would make some of the validation math easier?
second_integer = float(input("Input the second number (which is to be subtracted): "))
equation = float(first_integer)-second_integer
print("Result: "+str(equation))
