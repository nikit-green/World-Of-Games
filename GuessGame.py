import random


def play(difficulty):
    user_num = get_guess_from_user(difficulty)
    secret_num = generate_number(difficulty)
    result = compare_results(secret_num, user_num)
    if result:
        return "Damn, you're a psychic"
    else:
        return "Keep trying "


def generate_number(dif):
    secret_number = random.randint(0, dif + 1)
    return secret_number


def get_guess_from_user(dif):
    user_num = int(input(f"Please enter your guess between 0 - {dif + 1}: "))
    return user_num


def compare_results(secret_num, user_num):
    if secret_num != user_num:
        return False
    else:
        return True
