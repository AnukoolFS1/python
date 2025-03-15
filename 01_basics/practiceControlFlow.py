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


#Task3: Guess the number 

import random

runLoop = True

while runLoop:
    user_input = int(input("Guess a number: "))
    random_number = random.randint(1,10)

    if user_input == random_number:
        print("Congrats your guess was correct")
        runLoop = False
    else:
        print("Incorrect guess, please try again")
        print(random_number)