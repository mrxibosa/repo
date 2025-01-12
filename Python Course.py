# Variable = A container used to store a value (e.g., string, integer, float, or boolean).
#            Variables behave as if they are the value they store.

# Strings: Used to store text data.
first_name = "Bro"
food = "Pizza"
email = "Bro123@fake.com"

# Integers: Whole numbers, positive or negative, without a decimal.
age = 25
quantity = 3  # Corrected from float to int, as quantities are usually whole numbers.
number_of_students = 30

# Float: Decimal numbers, used for precision.
price = 30.50
gpa = 3.2
distance = 5.5

# Boolean: Represents True or False.
is_student = True
married = False

if is_student:
    print("You are a student")  # Executes if the condition (is_student == True) is met.

# Typecasting = Converting a variable from one data type to another (e.g., str(), int(), float(), bool()).

name = "Eric"
age = 27
gpa = 3.2
is_student = True

# Print the data type of the variable gpa.
print(type(gpa))

# Convert GPA from float to integer.
gpa = int(gpa)

# input() = Function that prompts the user to enter data.
#           Always returns the entered data as a string by default.

# Prompt the user to enter their name and age.
name = input("What is your name?: ")
age = int(input("How old are you?: "))  # Convert the input to an integer.

# Use f-strings for formatted output.
print(f"Hello {name}!")
print(f"You are {age} years old")

# Exercise 1 - Rectangle Area Calculator
# Prompts the user for the length and width of a rectangle, calculates its area, and displays it.

length = input("Enter the length:")  # Returns a string input.
width = input("Enter the width: ")  # Returns a string input.

# Convert string inputs to float for multiplication.
area = float(length) * float(width)

print(f"The area is {area} cm^2")  # Display the calculated area with units.

# Exercise 2 - Shopping Cart Program
# Prompts the user for an item, its price, and the quantity, then calculates the total cost.

item = input("What item would you like to buy? ")
price = float(input("What is the price?"))  # Convert price to a float for calculations.
quantity = int(input("How many would you like?"))  # Convert quantity to an integer.

# Calculate the total cost.
total = price * quantity

# Display the purchase details and the total cost.
print(f"You have bought {quantity} x {item}")
print(f"Your total is {total}")

# Madlibs Game
# A fun word game where the user provides random words to fill blanks in a story.

adjective = input("What animal do you like? ")  # Prompt for an adjective.
country = input("Which country is this beast from? ")  # Prompt for a country name.
cold_or_hot = input("Is it cold or hot in the country? Enter 'cold' or 'hot': ")  # Prompt for a climate descriptor.

# Display the story using the user's input.
print(f"Today I went to a {adjective} zoo")
print(f"The zoo had many beasts from {country}")
print(f"The country is {cold_or_hot}")

# Arithmetic and Math Operations
# Demonstrating how to perform basic arithmetic and compound assignments.

friends = 10  # Start with 10 friends.

# Increment the value of friends by 1.
friends = friends + 1  # Equivalent to friends += 1.
friends += 1

# Decrement the value of friends by 2.
friends = friends - 2  # Equivalent to friends -= 2.
friends -= 2

# Multiply the value of friends by 3.
friends = friends * 3  # Equivalent to friends *= 3.
friends *= 3

# Divide the value of friends by 2.
friends = friends / 2  # Equivalent to friends /= 2.
friends /= 2

# Raise friends to the power of 2.
friends **= 2

# Modulus: Calculate the remainder of friends divided by 2.
remainder = friends % 2  # Determines if the number is even or odd.

# Basic math operations.
a = 2
b = 3
c = -5
d = 4.67

# Perform various mathematical operations.
sum_ab = a + b  # Sum of a and b.
diff_ab = a - b  # Difference between a and b.
prod_ab = a * b  # Product of a and b.
quot_ab = a / b  # Quotient of a divided by b (float result).
int_quot_ab = a // b  # Integer division result.
remainder_ab = a % b  # Remainder of a divided by b.
power_ab = a ** b  # a raised to the power of b.
abs_c = abs(c)  # Absolute value of c.
rounded_d = round(d)  # Round d to the nearest integer.
max_value = max([a, b, c, d])  # Largest value among a, b, c, d.
min_value = min([a, b, c, d])  # Smallest value among a, b, c, d.
total_sum = sum([a, b, c])  # Sum of a, b, and c.
another_sum = pow(4, 3)  # 4 raised to the power of 3.

# Using the math module for advanced mathematical operations.
import math  # Import the math library for additional functions.

x = 9.9

# Print mathematical constants.
print(math.pi)  # Pi (3.14159...)
print(math.e)  # Euler's number (2.71828...)

# Square root of x.
result = math.sqrt(x)

# Round x up and down.
result = math.ceil(x)  # Round up to the nearest integer.
result = math.floor(x)  # Round down to the nearest integer.

# Using round() to round numbers.
y = 3.14159
rounded_value = round(y)  # Round to the nearest integer.
rounded_value_2 = round(y, 2)  # Round to 2 decimal places.

print(f"Rounded value: {rounded_value}")  # Display rounded integer.
print(f"Rounded value (2 decimal places): {rounded_value_2}")  # Display rounded float.

# Circumference Exercise
# Calculate the circumference of a circle given its radius.

# Prompt for the radius of the circle.
radius = float(input("Enter the radius of a circle: "))

# Calculate the circumference using the formula 2 * pi * radius.
circumference = 2 * math.pi * radius

# Display the circumference, rounded to 2 decimal places.
print(f"The circumference is: {round(circumference, 2)} cm")

# Radius Exercise
# Calculate the area of a circle given its radius.

# Prompt for the radius.
radius = float(input("What is the radius of the circle? "))

# Calculate the area using the formula pi * radius^2.
area = math.pi * pow(radius, 2)

# Display the area, rounded to 2 decimal places.
print(f"The area of the circle is {round(area, 2)} cm^2")

# Pythagorean Theorem Exercise
# Calculate the length of the hypotenuse given the lengths of the other two sides.

# Prompt for the lengths of sides A and B.
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

# Calculate the hypotenuse using the Pythagorean theorem.
c = math.sqrt(pow(a, 2) + pow(b, 2))

# Display the hypotenuse, rounded to 2 decimal places.
print(f"Side C: {round(c, 2)}")

# if-statements
# Execute code blocks based on conditions.

# Prompt the user to enter their age.
age = int(input("Enter your age: "))

# Check various conditions based on the entered age.
if age >= 100:
    print("You are too old to sign up!")  # For ages 100 and above.
elif age >= 18:
    print("You are now signed up!")  # For ages 18–99.
elif age < 0:
    print("You haven't been born yet!")  # For negative ages.
else:
    print("You must be 18+ to sign up.")  # For ages under 18.

# Food Prompt Exercise
# Simple yes/no prompt to determine food preference.

response = input("Would you like food? (Y/N): ")

# Check if the user responded "Y" (case-sensitive).
if response == "Y":
    print("Have some food!")  # Offer food if the response is "Y".
else:
    print("No food for you")  # Deny food for any other response.

# Validate User Input Exercise
# Ensure that the entered username adheres to specific rules.

# Prompt for a username.
username = input("Enter your username: ")

# Validate the username.
if len(username) > 12:  # Check if the length exceeds 12 characters.
    print("Your username can't be more than 12 characters.")
elif " " in username:  # Check if the username contains spaces.
    print("Your username can't contain spaces.")
elif not username.isalpha():  # Check if the username contains only letters.
    print("Your username can't contain numbers.")
else:
    print("Your username is valid.")  # Username is valid if all checks are passed.

# Indexing = Access elements of a sequence (like a string) using an index enclosed in square brackets [ ].
#            Indexing starts at 0 for the first element, and negative indexing starts at -1 for the last element.

# Set a sample credit card number as a string.
credit_number = "1234-5678-9012-3456"

# Access and display specific parts of the string using indexing and slicing.
print(credit_number[0])  # First character of the string.
print(credit_number[:4])  # First four characters of the string.
print(credit_number[5:9])  # Characters from index 5 to 8.
print(credit_number[5:])  # Characters from index 5 to the end of the string.
print(credit_number[-1])  # Last character of the string.
print(credit_number[::3])  # Every third character in the string.

# Reverse the string using slicing and display it.
last_digits = credit_number[::-1]
print(last_digits)


# Format Specifiers = Flags that format a value in specific ways within strings.
#                     They control alignment, decimal places, padding, signs, and more.

num = 1234.56789  # Sample number to demonstrate format specifiers.

# Examples of format specifiers with explanations:
formatted_num_1 = f"{num:.2f}"       # Limit to 2 decimal places: '1234.57'
formatted_num_2 = f"{num:10}"        # Right-align and allocate 10 spaces: '  1234.56789'
formatted_num_3 = f"{int(num):03}"   # Zero-pad to 3 digits: '001234'
formatted_num_4 = f"{num:<10}"       # Left-align and allocate 10 spaces: '1234.56789 '
formatted_num_5 = f"{num:>10}"       # Right-align and allocate 10 spaces: ' 1234.56789'
formatted_num_6 = f"{num:^10}"       # Center-align and allocate 10 spaces: ' 1234.56789 '
formatted_num_7 = f"{num:+}"         # Include '+' for positive numbers: '+1234.56789'
formatted_num_8 = f"{num:=+10}"      # Place '+' or '-' at the leftmost position: '+ 1234.56789'
formatted_num_9 = f"{num: }"         # Add a leading space for positive numbers: ' 1234.56789'
formatted_num_10 = f"{num:,}"        # Add a comma as a thousand separator: '1,234.56789'

# Print the formatted results with descriptions for clarity.
print(f"Fixed point (2 decimal places): {formatted_num_1}")
print(f"Right-align with 10 spaces: '{formatted_num_2}'")
print(f"Zero-padded integer: '{formatted_num_3}'")
print(f"Left-align with 10 spaces: '{formatted_num_4}'")
print(f"Right-align with 10 spaces: '{formatted_num_5}'")
print(f"Center-align with 10 spaces: '{formatted_num_6}'")
print(f"Include '+' for positives: '{formatted_num_7}'")
print(f"Sign leftmost in alignment: '{formatted_num_8}'")
print(f"Space for positives: '{formatted_num_9}'")
print(f"Comma separator: '{formatted_num_10}'")

# while Loop = Repeatedly execute a block of code while a condition remains True.

# Example: Prompt the user to enter their name until a valid input is provided.
name = input("Enter your name: ")
while name == "":  # Check if the user left the input blank.
    print("You did not enter your name.")
    name = input("Enter your name: ")  # Prompt again.

print(f"Hello, {name}!")  # Greet the user once a valid name is entered.

# Example: Validate the user's age to ensure it's not negative.
age = int(input("Enter your age: "))
while age < 0:  # Check if the age is invalid (negative).
    print("Age can't be negative.")
    age = int(input("Enter your age: "))  # Prompt again.

print(f"Your age is {age}.")

# Example: Repeatedly ask the user for food preferences until they type "q".
food = input("Enter a food you like (q to quit): ")

while food != "q":  # Continue until the user types "q".
    print(f"You like {food}.")
    food = input("Enter a food you like (q to quit): ")  # Prompt again.

print("Goodbye!")

# Example: Validate a number between 1 and 10.
num = int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:  # Check if the number is out of range.
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1 and 10: "))  # Prompt again.

print(f"Your number is {num}.")

# Compound Interest Calculator
# Calculate the final balance after applying compound interest for a given time.

# Initialize variables.
principal = 0  # Principal amount.
rate = 0  # Interest rate (in %).
time = 0  # Time period (in years).

# Input and validation for the principal amount.
while True:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero.")  # Reject invalid input.
    else:
        break  # Exit the loop once a valid principal is entered.

# Input and validation for the interest rate.
while True:
    rate = float(input("Enter the interest rate (in %): "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero.")  # Reject invalid input.
    else:
        break  # Exit the loop once a valid rate is entered.

# Input and validation for the time period.
while True:
    time = float(input("Enter the time period (in years): "))
    if time <= 0:
        print("Time can't be less than or equal to zero.")  # Reject invalid input.
    else:
        break  # Exit the loop once a valid time is entered.

# Calculate the total balance using the compound interest formula.
total = principal * pow(1 + rate / 100, time)

# Display the result rounded to 2 decimal places.
print(f"Balance after {time} years: ${total:.2f}")

# for Loops = Execute a block of code a fixed number of times.
#             Can iterate over ranges, sequences, or other iterable objects.

# Countdown from 10 to 1 using a for loop.
for x in reversed(range(1, 11)):
    print(x)

# Break the loop when a specific condition is met.
for x in range(1, 21):
    if x == 13:  # Stop the loop when x equals 13.
        break
    print(x)

# Countdown Timer Exercise
# A countdown timer that displays time in days, hours, minutes, and seconds.

import time  # Import the time module for delays.

# Prompt the user to enter the countdown duration in seconds.
my_time = int(input("Enter the countdown time in seconds: "))

# Countdown loop.
for x in reversed(range(0, my_time + 1)):
    seconds = x % 60  # Extract the seconds.
    minutes = (x // 60) % 60  # Extract the minutes.
    hours = (x // 3600) % 24  # Extract the hours.
    days = x // 86400  # Extract the days.
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")  # Format the time as DD:HH:MM:SS.
    time.sleep(1)  # Wait for 1 second between updates.

print("Time's up!")

# Nested Loops = A loop inside another loop. Useful for working with grids or repetitive patterns.

# Example: Print a grid of symbols.
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):  # Outer loop iterates over rows.
    for z in range(columns):  # Inner loop iterates over columns.
        print(symbol, end="")  # Print the symbol without a newline.
    print()  # Move to the next line after printing all columns in a row.

### Collections = Single "variables" used to store multiple values.

### Lists = Ordered, mutable, and allow duplicates.
fruits = ["banana", "cherry", "kiwi", "apple", "pear"]

# Replace the first element in the list.
fruits[0] = "pineapple"

# Add a new element to the end of the list.
fruits.append("grape")

# Remove the first occurrence of an element.
fruits.remove("apple")

# Insert an element at a specific position.
fruits.insert(0, "orange")

# Clear all elements from the list.
fruits.clear()

# Count the occurrences of a specific element.
pineapple_count = fruits.count("pineapple")

# Print the modified list and the count of "pineapple".
print(fruits)
print(f"Pineapple count: {pineapple_count}")

### SETS {} - unordered and immutable, but ADD and REMOVE OK, NO DUPLICATES.


# Define a set of fruits
fruits = {"banana", "cherry", "kiwi", "apple", "pear"}

# Add "pineapple" to the set
fruits.add("pineapple")

# Remove "apple" from the set
fruits.remove("apple")

# Remove and return an arbitrary element from the set
fruits.pop()

# Clear all elements from the set
fruits.clear()

# Print the resulting set
print(fruits)  # This will print an empty set since fruits.clear() was called

fruits = ("banana", "cherry", "kiwi", "apple", "pear")

print(fruits.index("apple"))
print(fruits.count("apple"))

for fruit in fruits:
    print(fruit)


foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit) ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

# Print each food item in the cart
for food in foods:
    print(food)

# Calculate the total price of all food items
for price in prices:
    total += price

print()  # Print an empty line for better readability

# Print the final total

print(f"Your total is ${total}")


### NESTED LIST

# Define a nested list of grocery items categorized into different groups
groceries = [
    ["apple", "orange", "banana", "coconut"],  # Group 1: Fruits
    ["celery", "carrots", "potatoes"],         # Group 2: Vegetables
    ["chicken", "fish", "turkey"]             # Group 3: Proteins
]

# Print the first item from the first group (fruits)
print(groceries[0][0])  # Output: "apple"


# Define a list of fruits
fruits = ["apple", "orange", "banana", "coconut"]

# Define a list of vegetables
vegetables = ["celery", "carrots", "potatoes"]

# Define a list of meats
meats = ["chicken", "fish", "turkey"]

# Combine the individual lists into a nested list called groceries
groceries = [fruits, vegetables, meats]

# Print the first item from the first list (fruits)
print(groceries[0][0])  # Output: "apple"


groceries = [
        ["apple", "orange", "banana", "coconut"],  # Group 1: Fruits
        ["celery", "carrots", "potatoes"],  # Group 2: Vegetables
        ["chicken", "fish", "turkey"]  # Group 3: Proteins
    ]

for collection in groceries:
        for food in collection:
            print(food, end=" ")

        print()


num_pad = ((1,2, 3),
           (4, 5, 6),
           (7, 8, 9),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# Python quiz game - Multiple choice questions

# Questions for the quiz
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

# Options for each question
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# Correct answers for each question
answers = ("C", "D", "A", "A", "B")
guesses = []  # List to store player's guesses
score = 0  # Variable to track the player's score
question_num = 0  # Variable to track the current question number

# Loop through each question
for question in questions:
    print("----------------")
    print(question)
    # Loop through the options for the current question
    for option in options[question_num]:
        print(option)

    # Get the player's guess and convert it to uppercase
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)  # Store the guess in the guesses list
    # Check if the guess is correct
    if guess == answers[question_num]:
        score += 1  # Increment the score if the answer is correct
        print("CORRECT!")
    else:
        print("INCORRECT!")
        # Print the correct answer if the guess is incorrect
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1  # Move to the next question

# Print the player's final score
print("----------------")
print(f"You got {score} out of {len(questions)} correct!")

### Dictionary = a collection of {key:value} pairs
#               ordered and changeable, no duplicates.

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exists!")
else:
    print("That capital does not exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear()

keys = capitals.keys()

print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

items = capitals.items()
print(items)

# Concession stand program
# Define the menu with items and their prices
menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []  # List to store items added to the cart
total = 0  # Variable to keep track of the total cost

# Print the menu
print("------MENU------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")

# Loop to take the user's order
while True:
    choice = input("What do you want? (type 'done' to finish): ").lower()
    if choice == 'done':
        break  # Exit the loop if the user is done ordering
    elif choice in menu:
        cart.append(choice)  # Add the item to the cart
        total += menu[choice]  # Add the item's price to the total
        print(f"{choice} added to your cart. Current total: ${total:.2f}")
    else:
        print("Sorry, that item is not on the menu.")  # Inform the user if the item is not found

# Print the order summary
print("\n------ORDER SUMMARY------")
for item in cart:
    print(item)
print(f"Total amount: ${total:.2f}")

