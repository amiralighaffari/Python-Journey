"""
Python Journey — Lessons 1–4
Practice archive by Amir

This file collects examples from the first four lessons.
Each section is a separate practice example; read and run sections individually.
"""

# ============================================================
# LESSON 1 — Input, variables, numbers, and arithmetic
# ============================================================

# Example 1: Divide two numbers
try:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    print(num1 / num2)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")
else:
    print("Calculation completed.")
finally:
    print("End of division example.")


# ============================================================
# LESSON 2 — Conditions, strings, and error handling
# ============================================================

# Example 2: Search for a name in a string (case-sensitive)
sentence = "my name is suzie"

if "jack" in sentence:
    print("Jack exists!")
elif "jake" in sentence:
    print("Jake is there.")
elif "Suzie" in sentence:
    print("Suzie exists.")
else:
    print("No matching name found.")


# Example 3: A simple calculator
try:
    print("Welcome to Amir's self-made calculator!")
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    operator = input("Enter an operator (+, -, *, /): ").strip()

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Wrong operator.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")


# Example 4: Case-insensitive search
sentence = "my name is jack and yours is jake"

if "jack" in sentence.upper():
    print("Jack was found.")
else:
    print("Jack was not found.")


# Example 5: Calculator with specific exception handling
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ").strip()

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Wrong operator.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid number entered.")


# ============================================================
# LESSON 3 — String methods and logical operators
# ============================================================

# Example 6: String methods
text = "some news about ...."
print(text.capitalize())
print(text.title())

# Other string-method practice:
# print(text.find("news"))
# print(text.count("news"))
# print(text.replace("news", "stories"))
# print(text.strip())


# Example 7: Replace a word (case-insensitive by converting to uppercase)
phrase = input("Enter a phrase: ")
phrase_upper = phrase.upper()

if "BAD" in phrase_upper:
    print(phrase_upper.replace("BAD", "..."))
    print("The text was edited!")
else:
    print("No bad word found.")


# Example 8: Simple login condition
user = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if (user == "admin" or user == "jack") and (
    password == "123" or password == "456"
):
    print("Login")
else:
    print("Invalid username or password.")


# Example 9: Another login-condition practice
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if (username == "jack" or username == "jake") and (
    password == "123" or password == "456"
):
    print("Login")
else:
    print("Wrong username or password.")


# ============================================================
# LESSON 4 — Conditional expressions, lists, and loops
# ============================================================

# Example 10: if/else
a = 12
b = 21

if a == b:
    print("OK")
else:
    print("NO")

# One-line conditional expression
print("OK") if a == b else print("NO")
print("YES") if 3 == 3 else print("NO")

# Nested conditional expression
print("=") if a == b else print("a is bigger") if a > b else print("b is bigger")

# Equivalent nested if statement
if a == b:
    print("=")
elif a > b:
    print("a is bigger")
else:
    print("b is bigger")


# Example 11: Basic list operations
data = [12, 15, 17, "reza", "ali"]
print(data.index(17))
data.append("333")
data.insert(2, 33)
print(data)

# Example 12: Removing matching items safely
data = [12, 15, 17, 12]
data = [item for item in data if item != 12]
print(data)


# Example 13: Grades list
grades = [12, 18, 15, 20, 12, 17, 20]
grades.append(19)
grades.insert(2, 10)
grades.remove(12)

print(grades)

if 20 in grades:
    print("20 exists!")

for grade in grades:
    print(grade)

# Print the indexes of all grades equal to 12
index = 0
for grade in grades:
    if grade == 12:
        print(index)
    index += 1


# Example 14: Nested lists
classes = [
    [12, 18, 15],
    [20, 17, 14],
    [10, 19, 16],
]
print(classes[2][1])
