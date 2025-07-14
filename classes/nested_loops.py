

def nestedLoops():
    for i in range(20):
        print("Hello, World!") # will get printed 20 times
        for y in range(2):
            print("Hello!") # will run 40 times

        print("foo") # will executed 20 times

    print("bar") # will execute 1 time


# Task: Print the multiplication table of the numbers 1 - 10

def multiplication_table():
    print("=== Multiplication Table ===")
    for i in range(1, 11):  # Numbers 1 to 10
        for j in range(1, 11):  # Multiply by 1 to 10
            print(f"{i} x {j} = {i*j} ")
        print()  # New line after each row

multiplication_table()