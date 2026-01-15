num = 524


def guess_number(num):
    while True:
        guess_number = int(input("guess the number: "))

        if(guess_number == num):
            print(f"You guess {guess_number}, it is right one")
            break

        elif guess_number > num:
            print(f"you guess {guess_number}, guess lower than {guess_number}")

        else:
            print(f"you guess {guess_number}, guess greater than {guess_number}")

print("guess number between 1 to 1000")
guess_number(num)