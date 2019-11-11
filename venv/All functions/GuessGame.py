import random

def guess():
    guess_number = random.randint(100,999)
    if len(set(str(guess_number))) == 3:
        return guess_number
    else:
        return guess()

guess_number = str(guess())
print(guess_number)
input_val = input("Enter your guess: ")
while guess_number != input_val:
    if guess_number[0] == input_val[0] or guess_number[2] == input_val[2]\
            or guess_number[1] == input_val[1]:
        print("Match")
        input_val = input("Enter your guess: ")
    elif guess_number[2] == input_val[0] and guess_number[0] == input_val[2]\
            and guess_number[1] == input_val[1]:
        print("Close")
        input_val = input("Enter your guess: ")
    else:
        print("Nope")
        input_val = input("Enter your guess: ")
else:
    print("Correct Number")


