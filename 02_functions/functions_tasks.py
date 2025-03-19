# print(sum([5,7],5))



def sum(a, b):
    return a + b

print(sum(2,5))



def check_prime(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    
    if is_prime:
        return "The given number is a prime number"
    else:
        return "The given number is not a prime number"
    
print(check_prime(int(input("Enter a number: "))))


def Maximum(list):
    biggest_number = 0
    for i in range(0, len(list)):
        print(list[i])
        if list[i] > biggest_number:
            biggest_number = list[i]
    
    return biggest_number

print(Maximum([4,3,5,2,1,4,0]))