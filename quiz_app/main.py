import random
import colorama

def main():
    score = 0
    while True:
        ans = outQuestion()
        user_ans = input("A. ")
        if user_ans == "exit()":
            break
        if ans == int(user_ans):
            print(colorama.Fore.GREEN + "Correct!" + colorama.Style.RESET_ALL)
            score = score + 1
        else:
            print(colorama.Fore.RED + "Wrong!" + colorama.Style.RESET_ALL)

    print("Your Score: " + str(score))


def outQuestion():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    op = ["+", "-", "/", "*"]
    opidx = random.randint(0, len(op) - 1)

    ques = str(num1) + " " + op[opidx]+ " " + str(num2)

    if op[opidx] == "+":
        ans = num1 + num2
    if op[opidx] == "-":
        ans = num1 - num2
    if op[opidx] == "/":
        ans = num1 / num2
    if op[opidx] == "*":
        ans = num1 * num2

    print("Q. " + ques)
    return int(ans)

main()
