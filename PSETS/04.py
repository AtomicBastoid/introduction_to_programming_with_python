# Task 04: number of vowels in string

myWord = "Igloo"
vowels = ["a", "e", "i", "o", "u"]

def countVowels():
    count = 0
    for char in myWord.lower():
        if char in vowels:
            count = count + 1
    print("Number of Vowels:", count)

def countConsonants():
    count = 0
    for char in myWord.lower():
        if char not in vowels:
            count = count + 1
    print("Number of Consonants:", count)

countVowels()
countConsonants()