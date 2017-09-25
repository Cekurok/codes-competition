N = input()

# Get the input
numArray = map(int, input().split())

sum_integer = 0

# Write the logic to add these numbers here
sum_integer = sum([x ** 2 for x in numArray])

# Print the sum
print(sum_integer)