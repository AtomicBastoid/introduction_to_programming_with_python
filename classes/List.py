grocery_list = ["egg","bread",100,9 ,  2.4,  True]

# # print(grocery_list)

# # grocery_list.append("Butter")
# # print(grocery_list)

# # grocery_list.remove(100)
# # print(grocery_list)

# grocery_list2 = grocery_list.copy()
# grocery_list2.append("Banana")
# grocery_list2.append(78)
# grocery_list2.append("peanut butter")

# print(grocery_list2)
# print(grocery_list)


# list1 = [1,2,3,"apple" , "banana",4]
# list2 = ["apple" , "banana",2,3, "orange","apple","banana"]
# list2.extend(list1)
# print(list2)

nested_list = [1,"ali", ["apple","banana", 23]]

print(len(nested_list))
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])

# Question:
# If the number is greater than 2 print numbers from list

Numbers = [0,1,5,2, 7, 0.75]

if Numbers[0] > 2:
    print(Numbers[0])
if Numbers[1] > 2:
    print(Numbers[1])
if Numbers[2] > 2:
    print(Numbers[2])
if Numbers[3] > 2:
    print(Numbers[3])
if Numbers[4] > 2:
    print(Numbers[4])
if Numbers[5] > 2:
    print(Numbers[5])


# Question:
# connentenate all chars to foem a string
char = ['h', 'e', 'l', 'l', 'o']

string = ""
string = string.join(char)
print(string)

# Question:
# check if "O" is in list
myList = ["H", "E", "L", "L", "O"]
if "O" in myList:
    print("O is in List")

# Question:
# if "I" in list conncantenate all strings in the list
myList2 = ["I", "G", "L", "O", "O"]
if "I" in myList2:
    print("".join(myList2)) 