# Define main function
def main():
    # Get user input
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    # most elegant way
    return n % 2 == 0

    # condensed version
    # return True if n % 2 == 0 else False

    # Using if else
    # if n % 2 == 0:
    #     return True  # return bool
    # else:
    #     return False


main()
