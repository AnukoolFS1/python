# Task 1: Even or Odd Checker
# num = int(input("Enter a number to check if it is an odd number or an even number: "))

# if num % 2 != 0:
#     print(f"{num} is an odd number")
# else:
#     print(f"{num} is an even number")

# Task 2: Sum of First N Numbers
# numTask = int(input("Enter a number to sum of its first numbers: "))

# result = 0
# for i in range(1, numTask + 1):
#     result += i

# print(result)


# Task3: Guess the number
# import random

# runLoop = True

# while runLoop:
#     try:
#         user_input = int(input("Guess a number: "))
#         random_number = random.randint(1,10)
#         if user_input == random_number:
#             print("Congrats your guess was correct")
#             runLoop = False
#         else:
#             print("Incorrect guess, please try again")
#             print(random_number)

#     except ValueError: # Handles  cases where input is not a number
#         print("Invalid input! Please enter a number between 1 to 10.")

# Task 4: Multiplication Table

# input_success = False
# number = 0

# while not(input_success):
#     try:
#         number = int(input("Enter a number for its table upto 10: "))
#         input_success = True
#     except ValueError:
#         print("Oops! you entered a wrong value. Please enter a number")

# table = 1

# while table <= 10:
#     print(f"{number} x {table} = {number * table}")
#     table += 1

# Task 5: Reverse a string
# string = input("Write a word: ")

# reveredString = ""

# for x in string:
#     reveredString = x + reveredString

# print(reveredString)

# practice control flow - Loops

# print even number upto 10
# for x in range(1, 11, -2):
#     print(x)

# # print each character in string "Python";

# for x in "Python":
#     print(x)

# # Find the sum of first natural numbers
# num = 1
# ans = 0
# while num <= 5:
#     ans += num
#     num += 1

# print(ans)

# practicing loop with break, continue and else

# break
for i in range(1, 10):
    if i == 6:
        break
    print(i)

# continue
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# else
for i in range(1,11):
    print(i)
else:
    print('Loop has been finished successfully')

# breaking the else
for i in range(1,11):
    if i == 3:
        break
    print(i)
else:
    print("Loop has been finished successfully")
