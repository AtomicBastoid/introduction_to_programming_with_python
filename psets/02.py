# Task 02: write a function that returns a square

# height = 2

# * * * *
# *     *
# *     *
# * * * *

def square(h=2):
    print("* " * (h +2))
    for i in range(1, h+1):
        print("*", end="")
        print(" " * (h + (h+1)), end="")
        print("*")
    print("* " * (h +2))

square("five")