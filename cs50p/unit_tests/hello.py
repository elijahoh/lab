def main():
    name = input("What's your name? ").strip()
    print(hello(name))


def hello(to="world"):
    if not to:
        to = "world"
    return f"Hello, {to}"


if __name__ == "__main__":
    main()
