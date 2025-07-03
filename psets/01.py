# Task 01: output a triangle of height n

# def tri(height):

# height = 5

def tri(height=5):
    for i in range(1,height+1):
        print(" " * (height - i), end="")
        print("*" * (2* i -1))

tri()