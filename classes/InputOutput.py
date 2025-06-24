marks = 100       ## This is known a direct assignment
name = input(" ") ## This is when you want to take input from the user note that there is no prompt present

## Ouput the value inside the variable
print(marks)  
print(name)


# IO practice

dostkanaam = input("aap ke dost ka kya naam hai: ") ## Example of input with a prompt

print("mere dost ka naam",dostkanaam,"hai") ## You can combine strings and variables in print statements using commas
print("mere dost ka naam" + dostkanaam + "hai") ## Using + instead of commas will not include spaces automatically

num = 7   ## This is an integer variable with the value 7
str = "7"  ## This is a string variable with the string "7"

## Triple quotes can be used for multi-line strings
myMultiLineStr = """
H
e
l
l
o
"""

input("New") ## This input is discarded by the program

print(myMultiLineStr) ## The multi-line string will be printed exactly as it is
print(num + num) ## This will perform arithmetic addition on the integers, resulting in 14
print(str + str) ## This will combine the strings, resulting in "77"