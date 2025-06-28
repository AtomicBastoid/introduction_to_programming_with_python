## Iterating through a range of numbers

# iterate from i = 0 to i = 3
for i in range(0, 4):
    print(i)

## Iterating through a list of strings
lst = ["Intro", "To", "Programming", "With", "Python"]

for i in lst:
    print(i)

# Iterating through a string
str = "Hello"

for i in str:
    print(i)

## Using break and continue

for i in range(0, 4):
    if i == 2:
        continue  # skip the value 2 and print the rest
    print(i)

for i in range(0, 4):
    if i == 2:
        break  # exit the loop when i is 2
    print(i)