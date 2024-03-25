from random import *


def draw_numbers():
    drawn = set()
    while len(drawn) < 6:
        drawn.add(randint(0, 60))
    return sorted(list(drawn))


def check_and_fix_input_numbers(numbers):
    new_numbers = []
    for num in numbers:
        if num.isalpha() or int(num) > 60:
            print("Invalid number detected!")
            return False
        else:
            new_numbers.append(int(num))
    return new_numbers


user_numbers = input("Pick 6 numbers between 0 and 60: ").split(",")
if len(user_numbers) != 6:
    print("You must pick 6 numbers")
else:
    if check_and_fix_input_numbers(user_numbers):
        new_user_numbers = check_and_fix_input_numbers(user_numbers)
        print(f"Your numbers are : {new_user_numbers}")
        cpu_numbers = draw_numbers()
        print(f"Drawn numbers : {cpu_numbers}")
        matched_numbers = list(set(new_user_numbers).intersection(set([cpu_numbers])))
        if len(matched_numbers) > 0:
            number = "number" if len(matched_numbers) == 1 else "numbers"
            print(f"You matched {len(matched_numbers)} {number} !!")
            print(f"Matched {number} : {matched_numbers}")
        else:
            print("You matched no numbers. Better luck next time!")
