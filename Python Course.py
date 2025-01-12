# Variable = A container for a value (string, integer, float, boolean)
#            Variables behave as if they the value they contain

# Strings
first_name = "Bro"
food = "Pizza"
email = "Bro123@fake.com"

# Integers
age = 25
quantity = 3.5
number_of_students = 30

# Float
price = 30.50
gpa = 3.2
distance = 5.5

# Boolean
is_student = True
married = False

if is_student:
    print("You are a student")

# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Eric"
age = 27
gpa = 3.2
is_student = True

print(type(gpa)) # to see the data type of the variable

gpa = int(gpa) # to convert GPA from float to integer

# input() = A function that prompts the user to enter data
#          Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))

print(f"Hello {name}!")   # f-strings - type f"whatever" to activate
print(f"You are {age} years old") # f-strings - type f"whatever" to activate

# Exercise 1 - The Rectangel Area Calculator

length = input("Enter the length:") # this returns a STRING
width = input("Enter the width: ") # this returns a STRING

area = float(length) * float(width)

print(f"The area is {area} cm^2")

# Exercise 2 - Shopping Cart Program

item = input("What item would you like to buy? ")
price = float(input("What is the price?"))
quantity = int(input("How many would you like?"))

total = price * quantity

print(f"You have bought {quantity} x {item}")
print(f"Your total is {total}")

# Madlibs game
# word game where you create a story
# by filling in blanks with random words

adjective = input("What animal do you like?")
country = input("Which country is this beast from?")
cold_or_hot = input("Is it cold or hot in the country? Enter cold or hot")

print(f"Today I went to a {adjective} zoo")
print(f"The zoo had many beasts from {country}")
print(f"The country is {cold_or_hot}")

# Arithmetic & Math
friends = 10

friends = friends + 1
friends += 1

friends = friends - 2
friends -= 2

friends = friends * 3
friends *= 3

friends = friends / 2
friends /= 2

friends **= 2
friends **= 2

remainder = friends % 2 # Modulus to decide if number is even or odd
                        # Remainder is 0 if number is even, 1 if number is odd

a = 2
b = 3
c = -5
d = 4.67

sum_ab = a + b  # Adds a and b, 5
diff_ab = a - b  # Subtracts b from a, -1
prod_ab = a * b  # Multiplies a and b, 6
quot_ab = a / b  # Divides a by b, approximately 0.6667
int_quot_ab = a // b  # Integer division of a by b, 0
remainder_ab = a % b  # Remainder when a is divided by b, 2
power_ab = a ** b  # a raised to the power of b, 8
abs_c = abs(c)  # Absolute value of c, 5
rounded_d = round(d)  # Rounds d to the nearest integer, 5
max_value = max([a, b, c, d])  # Returns the largest value, 4.67
min_value = min([a, b, c, d])  # Returns the smallest value, -5
total_sum = sum([a, b, c])  # Sum of a, b, and c, 0
another_sum = pow(4, 3)  # Raises the base 4 to the exponent 3, resulting in 4^3 = 64



import math  # Importing the math module which contains many mathematical functions

x = 9.9

# Print the value of pi (3.141592...)
print(math.pi)  # Prints the value of pi

# Print the value of e (2.71828...)
print(math.e)  # Prints the value of e (Euler's number)

# Calculate the square root of x and store the result in the variable result
result = math.sqrt(x)  # Calculates the square root of x

# Round x up to the nearest integer and store the result in the variable result
result = math.ceil(x)  # Rounds x up to the nearest integer

# Round x down to the nearest integer and store the result in the variable result
result = math.floor(x)  # Rounds x down to the nearest integer



# Using round() to round a number

y = 3.14159
rounded_value = round(y) # Rounds y to the nearest integer (3)

# Using round() to round a number to 2 decimal places (3.14)
rounded_value_2 = round(y, 2) # Rounds y to 2 decimal places (3.14)

# Print the rounded values
print(f"Rounded value: {rounded_value}") # Prints: Rounded value: 3
print(f"Rounded value (2 decimal places): {rounded_value_2}")  # Prints: Rounded value (2 decimal places): 3.14

### Circumference exercise

import math  # Importing the math module to use mathematical functions and constants

# Prompt the user to enter the radius of a circle
radius = float(input("Enter the radius of a circle: "))

# Calculate the circumference of the circle using the formula 2 * pi * radius
circumference = 2 * math.pi * radius

# Print the calculated circumference, rounded to 2 decimal places
print(f"The circumference is: {round(circumference, 2)}cm")


## Radius exercise

import math  # Importing the math module to use mathematical functions and constants

# Prompt the user to enter the radius of the circle
radius = float(input("What is the radius of the circle? "))

# Calculate the area of the circle using the formula pi * radius^2
area = math.pi * pow(radius, 2)

# Print the calculated area, rounded to 2 decimal places
print(f"The area of the circle is {round(area, 2)}cm^2")


import math  # Importing the math module to use mathematical functions and constants

# Prompt the user to enter the lengths of sides A and B
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

# Calculate the length of the hypotenuse (side C) using the Pythagorean theorem
c = math.sqrt(pow(a, 2) + pow(b, 2))

# Print the calculated length of the hypotenuse, rounded to 2 decimal places
print(f"Side C: {round(c, 2)}")

### if-statements = do some code ONLY IF some condition is True
#                 = Else do something else

age = int(input("Enter your age: "))  # Prompt the user to enter their age

if age >= 100:
    print("You are too old to sign up!")  # Message for users 100 years old or older
elif age >= 18:
    print("You are now signed up!")  # Message for users between 18 and 99 years old
elif age < 0:
    print("You haven't been born yet!")  # Message for users with a negative age
else:
    print("You must be 18+ to sign up.")  # Message for users younger than 18

# Exercise 1

# Prompt the user with a question and store their response
response = input("Would you like food? (Y/N): ")

# Check if the response is "Y"
if response == "Y":
    print("Have some food!")  # If the user responds with "Y", print this message
else:
    print("No food for you")  # If the user responds with anything other than "Y", print this message


name = input("Enter your name: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

### Calculator Exercise

# Prompt the user to enter the first and second numbers
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Prompt the user to choose an operator
operator = input("Enter an operator (+, -, *, /): ")

# Check which operator the user has chosen and perform the corresponding operation
if operator == "+":
    result = num1 + num2  # Add num1 and num2
    print(round(result, 3))  # Print the result rounded to 3 decimal places
elif operator == "-":
    result = num1 - num2  # Subtract num2 from num1
    print(round(result, 3))  # Print the result rounded to 3 decimal places
elif operator == "*":
    result = num1 * num2  # Multiply num1 by num2
    print(round(result, 3))  # Print the result rounded to 3 decimal places
elif operator == "/":
    result = num1 / num2  # Divide num1 by num2
    print(round(result, 3))  # Print the result rounded to 3 decimal places
else:
    print("Invalid operator")  # Print an error message if the operator is invalid

### Weight Converter Exercise

# Prompt the user to enter their weight
weight = float(input("Enter your weight: "))

# Prompt the user to specify the unit (Kilograms or Pounds)
unit = input("Kilograms or Pounds? (K or L): ")

# Check the unit and perform the corresponding conversion
if unit == "K":
    weight = weight * 2.205  # Convert weight from kilograms to pounds
    unit = "Lbs."  # Update the unit to pounds
elif unit == "L":
    weight = weight / 2.205  # Convert weight from pounds to kilograms
    unit = "Kg"  # Update the unit to kilograms
else:
    print(f"{unit} was not valid")  # Print an error message if the unit is invalid

# Print the converted weight and unit
print(f"The converted weight is: {weight} {unit}")

# Temperature Converter Exercise

# Prompt the user to specify the unit (Celsius or Fahrenheit)
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

# Prompt the user to enter the temperature value
temp = float(input("Enter the temperature: "))

# Check if the unit is Celsius
if unit == "C":
    # Convert Celsius to Fahrenheit using the formula
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")  # Print the converted temperature

# Check if the unit is Fahrenheit
elif unit == "F":
    # Convert Fahrenheit to Celsius using the formula
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")  # Print the converted temperature

# If the unit is invalid
else:
    print(f"{unit} is an invalid unit of measurement")  # Print an error message



# Logical operators = evaluate multiple conditions (or, and, not)
#                     or  = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)


# OR
temp = 25  # Set the temperature to 25

is_raining = False  # Set the raining status to False

# Check if the temperature is greater than 35, less than 0, or if it is raining
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")  # If any condition is true, print this message
else:
    print("The outdoor is still scheduled")

# AND

temp = 30  # Set the temperature to 30
is_sunny = True  # Set the sunny status to True

# Check if the temperature is greater than or equal to 28 and if it is sunny
if temp >= 28 and is_sunny:
    print("It is HOT outside 😡")  # Print this message if it is hot
    print("It is SUNNY 🌞")  # Print this message if it is sunny
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")  # Print this message if it is cold
    print("It is SUNNY 🌞")  # Print this message if it is sunny

## Weather Exercise

temp = 1  # Set the temperature to 1
is_sunny = True  # Set the sunny status to True

# Check if the temperature is greater than or equal to 28
if temp >= 28:
    print("It is HOT outside 😡")  # Print this message if it is hot
    if is_sunny:
        print("It is SUNNY 🌞")  # Print this message if it is sunny
    else:
        print("It is CLOUDY ☁️")  # Print this message if it is cloudy
# Check if the temperature is less than or equal to 0
elif temp <= 0:
    print("It is COLD outside 🥶")  # Print this message if it is cold
    if is_sunny:
        print("It is SUNNY 🌞")  # Print this message if it is sunny
    else:
        print("It is CLOUDY ☁️")  # Print this message if it is cloudy
# Check if the temperature is between 0 and 28 (excluding 0)
elif 0 < temp < 28:
    print("It is COLD outside 😊")  # Print this message if it is warm
    if is_sunny:
        print("It is SUNNY 🌞")  # Print this message if it is

# NOT
# Initialize a variable to store whether it's sunny or not
is_sunny = True  # It is sunny

# Use the not operator to check if it is not sunny
if not is_sunny:
    print("It is not sunny outside")  # Print this message if it is not sunny
else:
    print("It is sunny outside")  # Print this message if it is sunny

### Conditional Expression = A one line shortcut for the if-else statement (ternary operator)
                        # Print or assign one of two values based on a condition
                        # X if condition else Y
# Positive
num = -5  # Set the number to -5

# Print "Positive" if num is greater than 0, otherwise print "Negative"
print("Positive" if num > 0 else "Negative")

# Even or Odd
num = 6  # Set the number to 6
a = 6  # Set the first number to 6
b = 7  # Set the second number to 7
age = 27
temperature = 27
user_role = "admin"

# Print "Even" if num is divisible by 2 with no remainder, otherwise print "Odd"
print("Even" if num % 2 == 0 else "Odd")

# Determine the maximum of the two numbers a and b
max_num = a if a > b else b
# Determine the minimum of the two numbers a and b
min_num = a if a < b else b

# Print the maximum and minimum numbers
print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")
status = "Adult" if age >= 18 else "Child"
weather = "Hot" if temperature >= 23 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

### String Methods

# Prompt the user to enter their name and phone number
name = input("What is your name?\n")
phone_number = input("Enter your phone #: ")

# Calculate the number of characters in the name
characters = len(name)

# Find the position of the first empty string (should be -1 since it's not a valid search)
tame = name.find("")

# Find the position of the last occurrence of "E"
rame = name.rfind("E")

# Capitalize the first letter of the name
game = name.capitalize()

# Convert the name to uppercase
bame = name.upper()

# Convert the name to lowercase
zame = name.lower()

# Check if the name is composed of digits only
lame = name.isdigit()

# Check if the name is composed of alphabetic characters only
vame = name.isalpha()

# Count the number of hyphens in the phone number
qame = phone_number.count("-")

# Replace hyphens with spaces in the phone number
phone_number = phone_number.replace("-", " ")

# Print the modified phone number
print(phone_number)

# Print the number of characters in the name
print(f"Your name has {characters} characters")

print(help(str))