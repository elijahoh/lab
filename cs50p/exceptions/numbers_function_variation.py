def main():
    x = get_num()
    print(f"x is {x}")


def get_num():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass


main()
