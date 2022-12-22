import random


def generate_random():
    value = random.randint(0,1)
    if value == 1:
        return "*"
    return " "


def mount_board():
    board = ""
    for _ in range(5):
        for _ in range(5):
            board+= generate_random()
        board+="\n"
    return board