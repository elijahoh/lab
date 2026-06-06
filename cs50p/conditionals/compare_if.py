# Get user's input
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is lesser than y.")
elif x > y:
    print("x is greater than y.")
else:  # elif x == y:
    print("x is equal to y.")
