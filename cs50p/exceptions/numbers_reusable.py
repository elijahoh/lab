def main():
    x = get_num("What's x? ")
    print(f"x is {x}")


def get_num(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
