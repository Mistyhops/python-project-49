import random

from brain_games.utils import int_input_answer, check_answer


def gcd_game(username: str):
    print("Find the greatest common divisor of given numbers.")

    for _ in range(3):
        first_value, second_value = random.randint(1, 30), random.randint(1, 30)
        correct_answer = None

        for i in range(max(first_value, second_value), 0, -1):
            if first_value % i == 0 and second_value % i == 0:
                correct_answer = i
                break

        print(f"Question: {first_value} {second_value}")

        user_answer = int_input_answer()

        if not check_answer(
                user_answer=user_answer,
                correct_answer=correct_answer,
                username=username,
        ):
            break
    else:
        print(f"Congratulations, {username}!")
