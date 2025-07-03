# Task 05: Money Change Problem

# money = 100, 50, 10, 5, 1

def returnChange(num):
    hundread = num // 100
    num = num - (hundread * 100)
    fifty = num // 50
    num = num - (fifty * 50)
    ten = num // 10
    num = num - (ten * 10)
    five = num // 5
    num = num - (five * 5)
    one = num // 1
    num = num - (one) 

    print("hundread:", hundread, "fifty:", fifty, "ten:", ten, "one:", one)

def returnChange(num): # efficient
    change = {}
    money = [100, 50, 10, 5, 1]

    for coin in money:
        if num >= coin:
            num_coin = num // coin
            change[coin] = num_coin
            num = num - num_coin * coin
    
    print("Change Returned:", change)

returnChange(354)