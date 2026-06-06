# Ask user for their name, remove whitespace and capitalize user's name
name = input("What's your name? ").strip().title()

# Remove whitespace from str and capitalize user's name
# name = name.strip().title()

# Capitalize user's name
# name = name.title()

# Split user name into first and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}! Your last name is {last}.")
