import random

import prompt


def welcome_script() -> str:
    welcome_message = f"Welcome to the Brain Games!"
    print(welcome_message)

    name_input_message = f"May I have your name? "
    username = input(name_input_message)

    print(f"Hello, {username}")

    return username


def is_even_game(username: str):
    string_answer = {
        True: 'yes',
        False: 'no',
    }

    value = random.randint(1, 1000)
    print(f"Question: {value}")
    is_even = string_answer.get(value % 2 == 0)
    user_answer = prompt.string("Your answer: ")

    if user_answer == is_even:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{is_even}'.\n"
              f"Let's try again, {username}!")
        return False
