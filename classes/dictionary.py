my_dict ={"pakistan":'karachi',"usa":'new york','france':'london'} # basic dictionary initialization
print(my_dict) # prints the dictionary
print(len(my_dict)) # prints the length of the dictionary


# #accessing values via keys
print(my_dict['pakistan'])
print(my_dict['usa'])
print(my_dict['france'])

print(my_dict['England'])# keyerror because the key is not present in the dictionary


print(my_dict.keys()) # prints the keys of the dictionary
print(my_dict.values()) # prints the values of the dictionary


print(my_dict.get('India'))  # output : none
print(my_dict.get('usa'))


dictionary={} # empty dictionary initialization
dictionary [10]='2' # adding a key-value pair to the dictionary
print(dictionary) # printing the updated dictionary

# combining two dictionaries into One
my_dict= {"name": "John","age":25, "city": "New York"}
dict1={'a':1,'b':2}
dict2={'b':3, 'c':4}
combined_dict={**dict2,**dict1}
print(combined_dict)

# creating a new dictionary
car={'make':'Toyota', 'model':'Corolla','year':'2020'}
print(car['year']) # accessing the value of the key 'year'

# updating the key present in the dictionary
student={'name':'Alice','grade':'A'}
student['grade']='B'
print(student)

# adding a new key-value pair to the dictionary
book={'title':'1984', 'author':'George'}
book['year']='1949'
book['version']="4th"
print(book)

# removing a key-value pair from the dictionary
product={'name':'Laptop', 'price':1500,'stock':30}
del product['stock']
print(product)

# creating a dictionary with (fromkeys) method
my_dict=('1', '2','3','4')
dictionary=dict.fromkeys(my_dict, 6) # yh my_dict ki keys ko 6 se initialize kr dega yani 6 unki values ho jayengi
print(dictionary)


dictionary=["name","age"]
updated_dictionary = dict.fromkeys(dictionary,"Sara")
updated_dictionary["age"]= 25
print(updated_dictionary)

def sort(my_list = ["eishal", "nazim", "keshwani"]):
    dictionary = {}
    for i in range(len(my_list)):
        dictionary[i] = my_list[i]

    return dictionary

print(sort())

#methods of dictionary
print(my_dict.keys()) #fetches keys
print(my_dict.values()) #fetches values
print(my_dict.items()) #fetches key-value pair
print(my_dict.get('usa')) #fetches the value if present
print(my_dict.get('india')) #no error

# updating a dictionary using (update) method
my_data = {"iran": "tehran", "uae":"dubai", "karachi": "new york", "south korea": "seoul"}
my_dict.update(my_data)
print(my_dict)

