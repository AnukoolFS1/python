print("Hello, Python!")

# variables
name = "Anukool"
age = 25
is_developer = True

# Data Types
"Anukool"  # string
25  # number
25.5  # Float
True
False  # boolean
[1, 2, 3]  # List (array in js)
(1, 2, 3, 4)  # tuple``
{"name": "Anukool", "age": 25}  # Dictionary (Object in js)

# Input Output
# sName = input("What's your name? ")
# print("Hello ",sName)

# f-string (Format String)(f"") similar to template literals in js
# use f followed by double quotes
print(f"hello my name is {name} and I am {age} years old")

# Type Casting / Type Conversion
a = int("25")
b = float("25.5")
c = bool("true")
s = str(20)


# Multiple Inputs in one line
d, e = input("Enter two number seperated by space ").split()

d = int(d)
e = int(e)

print(f"The sum of the two numbers is {d + e}")

# Constant (just an convention in python)
PI = 3.14
GRAVITY = 9.8
# these are the just convention and not strict you can a it later but
# the tradition say to not and to recognise that the variable should not
# change
