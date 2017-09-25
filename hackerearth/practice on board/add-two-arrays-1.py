N = int(input())

# Get the array 
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

# Write the logic here:
sumArray = [x+y for x,y in zip(numArray1,numArray2)]

# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")