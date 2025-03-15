# Arithmetic Operators
a = 10
b = 3

print(a + b) # addition +
print(a - b) # subtraction -
print(a * b) # multiplication *
print(a / b) # division /
print(a // b) # floor division //
print(a % b) # modulus %
print(a ** b) # exponentiation **

# Comparison Operators
print(a == b) # equal to ==
print(a != b) # not equal to !=
print(a > b) # greater than >
print(a < b) # less than <
print(a >= b) # greater than or equal to
print(a <= b) # less than or equal to


# Logical Operators
print(10>5 and 5>2) # logical and "and" (just like && in js)
print(5>4 or 20 < 15) # logical or "or" (just like || in js)
print(not(10 > 5)) # logical not "not(expression)" (just like ! in js) 

# Assinment Operators
# the most basic "=" assin operator
# a += 10 == a = a + 10
# in similar way -=, *=, /=

# Membership Operators 
# This is super useful in Python when checking if a value exists in 
# list, string, tuple
print("a" in "apple") # in -- True since it exist
print("z" not in "apple") # not in -- True since it does not exist
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # True
print("grapes" not in fruits) # True

# Identity Operators
# These operators compare the memory location of two objects.
# In JS this is similar to === (strict equality).
# is -- Objects are identical -- a is b -- True
# is not -- Object are not identical -- a is not b -- False
d = [1,2,3]
e = d

print(e is d) # True
print(e is not d) # False


# Ternary Operator
age = 20
result = "adult" if age > 18 else "minor" # like age > 18? "adult" : "minor"
print(result)
