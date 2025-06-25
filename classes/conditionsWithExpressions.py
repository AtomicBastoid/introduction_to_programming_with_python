# # > : greater than
# if 10 > 9: # True
#     print("10 is greater than 9")

# # < : less than
# if 10 < 9: # False
#     print("10 is less than 9")

# # <= : less than equal to
# if 8 <= 7: # False
#     print("8 is less than equal to 7")

# if 8 <= 8: # True
#     print("8 is less than equal to 7")

# # >= : greater than equal to
# if 8 >= 7: # True
#     print("8 is less than equal to 7")

# if 8 >= 8: # True
#     print("8 is less than equal to 7")

# if 8 >= 9: # False
#     print("8 is less than equal to 7")

# # == : equal to
# if 10 == 9.999999: # False
#     print("10 is equal to 9")

# # != : not equal to
# if 10 != 9.99999: # True
#     print("10 is not equal to 9.999999")



age = input("your age: ")

# if...elif...else
if age >= 63: # False
    print("Senior")
elif age >= 20: # False
    print("Middle")
elif age >= 13: # True
    print("Teen")
elif age <= 12:
    print("Child")