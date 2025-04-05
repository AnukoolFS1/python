s1 = 'hello' # single quote 
s2 = "Python" # double quote still the same string data type
s3 = '''multi line 
string in python''' # multi line strings

concate_str = "Hello" + " " + "Python" # Basic concatenation

# print(concate_str)

#repetition
# print("python " * 4) # 'python python python python'

#indexing
s = 'PythonIsGood'
s[0] # 'P'
s[-1] # "g"

#Slicing
# print(s[2:10]) # 'thonIsGo'
# print(s[2:]) # 'py'is sliced so 'thonIsGood' is result
# print(s[:10]) # 'od' is sliced so 'PythonIsGood' is result


# loop over strings

# for char in 'Python':
    # print(char)
# P
# y
# t
# h
# o
# n


# length and membership
# print(len(s)) # length of the string

# print('P' in s) # member of s
# print('Z' not in s) # not member of s


# Case Methods
example_string = "example"
print(example_string.upper()) # return the uppercase for the string
print(example_string) # now it will not affect the original string 
 # similarly we have lower and capitailze method
example_string2 = "EXAMPLE ONE"
print(example_string2.lower())
print(example_string2.capitalize()) # capitalize by whole
print(example_string2.title()) # capitalize by word
example_string3 = "ExaMple TWo"
print(example_string3.swapcase()) # swap => eXAmPLE twO

# formatting
console_log = "Hello, {}".format("Anukool")
print(console_log)

console_log = "Hello, %s" % "Chauhan"
print(console_log)


