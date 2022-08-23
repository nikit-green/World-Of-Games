import random
import requests


def play(difficulty):
    random_num = random.randint(0, 100)
    actual_res = get_money_interval(random_num, difficulty)
    user_guess = get_guess_from_user(random_num)
    if user_guess in actual_res:
        return "Nice, you should start an exchange shop"
    else:
        return "Nope, you should contact your bank"

def get_money_interval(random_num, d):
    url = f"https://api.apilayer.com/fixer/convert?to=ILS&from=USD&amount={random_num}"
    payload = {}
    headers = {"apikey": "g25i89awfgRjHwQbkHfdIb14Am2y7ozj"}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()["result"]
    num_interval = range(int(result) - (5 - d), int(result) + (5 - d))
    return num_interval


def get_guess_from_user(random_num):
    user_guess = int(input(f"Guess how much {random_num} USD will be in ISL: "))
    return user_guess
