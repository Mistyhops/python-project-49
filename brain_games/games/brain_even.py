import random

import prompt

from brain_games.utils import STRING_ANSWER, check_answer


def is_even_game(username: str):
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    for _ in range(3):
        value = random.randint(1, 1000)
        print(f"Question: {value}")
        is_even = STRING_ANSWER.get(value % 2 == 0)
        user_answer = prompt.string("Your answer: ")

        if not check_answer(
                user_answer=user_answer,
                correct_answer=is_even,
                username=username,
        ):
            break
    else:
        print(f"Congratulations, {username}!")
