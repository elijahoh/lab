# Get input from user for integers
# x = int(input("What's x? "))
# y = int(input("What's y: "))

# print(x + y)

# Get input from user for float
x = float(input("What's x? "))
y = float(input("What's y: "))

# round the result to 2 decimal places
z = round(x + y, 2)

# Add formating to the output eg. 1,000
print(f"{z:,}")

# Add formating to print to 2 decimal places
# print(f"{z:.2f}")
