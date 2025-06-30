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


'''Task: 01
consider a list of your choice and print start three elements'''
list =["apple","mango","banana", "orange","peach","pineapple"]

# for last 3 elements
for i in range(0,6):
    if i < 3:
        continue
    print(list[i])
    
## The while loop

number = 1

while number < 3:
    print(number)
    number = number + 1

# Using else statement also works with while loop
counter = 0

while counter < 2:
    print("inside loop")
    counter = counter + 1
else:
    print("Outside Loop")

number = int(input('Enter a number: '))
i = 0

while i < number:
    print(i)
    i = i + 1


# Infinite loop example
age = 32

while age > 18:
    print("You are an adult.")

# This is equivalent to:
usrinput = ""

while True:
    print("this")
    usrinput = input("type exit if you want the loop to stop: ")
    if usrinput == "exit":
        break


'''Task: 02
Take input from the user as to how many elements they want to print from the list'''
list =["apple","mango","banana", "orange","peach","pineapple"]

ask = int(input("How many elements do you want to print: "))
i = 0

while i < ask:
    print(list[i])
    i = i + 1