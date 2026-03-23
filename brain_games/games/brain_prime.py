import random

import prompt

from brain_games.utils import STRING_ANSWER, is_prime_number, check_answer


def is_prime_game(username: str):
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")

    for _ in range(3):
        value = random.randint(1, 30)
        print(f"Question: {value}")

        is_prime = STRING_ANSWER.get(is_prime_number(value))
        user_answer = prompt.string("Your answer: ")

        if not check_answer(
                user_answer=user_answer,
                correct_answer=is_prime,
                username=username,
        ):
            break
    else:
        print(f"Congratulations, {username}!")
