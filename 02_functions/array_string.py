def mutate_string(string, position, character):
    a = list(string)
    a.insert(position, character)
    return "".join(a)

print(mutate_string("abracadabra", 5, "k"))


# a = [1,2,3,4,5,6]

# a(2) = "55"

# print(a) IBM is here 