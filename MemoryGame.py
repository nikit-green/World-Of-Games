import random
from tkinter import *


def play(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    result = is_list_equal(random_list, user_list)
    if result:
        return "Your memory is elephant like"
    else:
        return "Go test for Alzheimer's disease"


def is_list_equal(random_list, user_list):
    random_list.sort()
    user_list.sort()
    if random_list == user_list:
        return True
    else:
        return False


def get_list_from_user(difficulty):
    user_list = []
    for i in range(0, difficulty):
        user_num = int(input("Please enter your guess number: "))
        user_list.append(user_num)
    return user_list


def generate_sequence(difficulty):
    list_of_numbers = [random.randint(0, 101) for i in range(difficulty)]
    win = Tk()
    win.geometry("300x68")
    Label(win, text=f"{list_of_numbers}  ", font='Helvetica 20 bold').pack(pady=20)
    win.after(700, lambda: win.destroy())
    win.mainloop()
    return list_of_numbers
