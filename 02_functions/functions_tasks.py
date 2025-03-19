# print(sum([5,7],5))
import math


def add_numbers(a, b):
    return a + b


print(add_numbers(2, 5))


def check_prime(number):
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return "The given number is not a prime number"

    return "The given number is  a prime number"


print(check_prime(int(input("Enter a number: "))))


def Maximum(list):
    if not list:
        return "the list is empty"

    biggest_number = list[0]
    for num in range(list):
        if num > biggest_number:
            biggest_number = num

    return biggest_number


print(Maximum([4, 3, 5, 2, 1, 4, 0]))
