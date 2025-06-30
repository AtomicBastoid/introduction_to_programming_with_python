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


## The while loop

number = 1

while number <= 3:
    print(number)
    number = number + 1

# Using else statement also works with while loop
counter = 0

while counter < 2:
    print("inside loop")
    counter = counter + 1
else:
    print("Outside Loop")

# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print('You entered:', number)
    number = int(input('Enter a number: '))

print('The end.')

# Infinite loop example
age = 32

while age > 18:
    print("You are an adult.")

# This is equivalent to:
while True:
    print("You are an adult.")
