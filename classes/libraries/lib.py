import random

def greet():
    name = input("Your Name is: ")
    print("Hello " + name)

def isAdult(age : int) -> bool: 
    if age >= 18:
        return True
    return False

def getAge() -> int:
    return int(input("Your Age is:"))

def joinList(array : list) -> str:
    return "".join(array)

def motivate():
    motivational_quotes = [
        "Code is like humor. When you have to explain it, it’s bad. – Cory House",
        "The best error message is the one that never shows up. – Thomas Fuchs",
        "Experience is the name everyone gives to their mistakes. – Oscar Wilde",
        "The function of good software is to make the complex appear simple. – Grady Booch",
        "First, solve the problem. Then, write the code. – John Johnson",
        "Programs must be written for people to read, and only incidentally for machines to execute. – Harold Abelson",
        "Learning to write programs stretches your mind and helps you think better. – Bill Gates",
        "Don't worry if it doesn't work right. If everything did, you'd be out of a job. – Mosher’s Law",
        "If you can’t explain it simply, you don’t understand it well enough. – Albert Einstein",
        "Success is the sum of small efforts, repeated day in and day out. – Robert Collier"
    ]
    print()
    print(motivational_quotes[random.randint(0, 9)])
    print()
