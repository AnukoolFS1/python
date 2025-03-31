# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    S = input()
    
    # Extract even and odd indexed characters
    even_chars = S[0::2]  # Characters at index 0, 2, 4, ...
    odd_chars = S[1::2]   # Characters at index 1, 3, 5, ...
    
    # Print the result
    print(even_chars, odd_chars)
