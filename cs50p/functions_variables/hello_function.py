# Define main function
def main():

    # Get iput from user
    name = input("What is your name? ")
    hello(name)


# Define hello with a default value "world"
def hello(to="world"):
    print(f"Hello, {to}")


# Print with default "world"
hello()

# Calling main function
main()
