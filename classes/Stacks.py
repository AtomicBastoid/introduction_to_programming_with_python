# Step 1: Create an empty stack
# stack = [] # initializing stack
# print("Initial stack:", stack)

# # Step 2: Push elements using append()
# stack.append(10) # Add elements to stack
# stack.append(20) # Add elements to stack
# stack.append(30) # Add elements to stack

# print("Stack after pushes:", stack)

# # Step 3: Pop the top element
# # Pop will remove elements from stack from the top using .pop()
# top = stack.pop() 
# print("Popped element:", top)
# print("Stack after pop:", stack)



# # Step 4: Peek at the top (without removing it)
# # python donot support peek function so we will define it using a condition and it will return the top value of stack
# if len(stack) > 0:
#     print("Top element (peek):", stack[-1])
# else:
#     print("Stack is empty")


# # Step 5: Check if the stack is empty
# # Again python donot supprot isempty() function so for performing this task we will define some condition to check if the stack we define is empty or not
# if len(stack) == 0:
#     print("Stack is empty")
# else:
#     print("Stack is not empty")


# # Step 6: Display stack elements (top to bottom)
# # this will print the elements of stack from top to bottom
# print("Stack (top -> bottom):")
# for item in reversed(stack):
#     print(item)


# # these are the functions designed to perform the same task discussed above 
stack = [] # the is the initial stack
# Functions for above method

# Function to add elements in the stack
def push(stack, item):
    stack.append(item)
    # print(f"Pushed {item}")
    print("Pushed", item)

# calling functions and adding elemnts to stack
push(stack, 40)
push(stack, 50)
print(stack)

# remove the elments from stack 
# def pop(stack):
#     if len(stack) == 0: # here it will check if the stack is empty it will print stack is empty 
#         print("Stack Empty")
#         return None # if stack is empty function will return to this statement and function ends here
#     return stack.pop() # if stack is not empty function will remove/pop element from the top

# we have print the function because we have used return statement  in our function definition
# print(pop(stack))
# print(stack)


# finding the top element in stack
def peek(stack):
    if len(stack) > 0: # here it will check if the length of stack is greater then "0" it will return the -1 (last/top element) of the stack
        print(stack[-1])
    else:
        print("Empty Stack")

# peek function is called here
peek(stack)

# display the elements of stack from top to bottom
def display(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack (top → bottom):")
        for item in reversed(stack):
            print(item)


# push(stack, 40)
# push(stack, 50)
# display(stack)
# print("Top:", peek(stack))
# print("Popped:", pop(stack))
display(stack)
