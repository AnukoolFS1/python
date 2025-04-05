s1 = 'hello' # single quote 
s2 = "Python" # double quote still the same string data type
s3 = '''multi line 
string in python''' # multi line strings

concate_str = "Hello" + " " + "Python" # Basic concatenation

print(concate_str)

#repetition
print("python " * 4) # 'python python python python'

#indexing
s = 'PythonIsGood'
s[0] # 'P'
s[-1] # "g"

#Slicing
print(s[2:10]) # 'thonIsGo'
print(s[2:]) # 'py'is sliced so 'thonIsGood' is result
print(s[:10]) # 'od' is sliced so 'PythonIsGood' is result


# loop over strings

for char in 'Python':
    print(char)
# P
# y
# t
# h
# o
# n


# length and membership
print(len(s)) # length of the string

print('P' in s) # member of s
print('Z' not in s) # not member of s
    