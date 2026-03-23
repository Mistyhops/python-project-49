import random

from brain_games.utils import int_input_answer, check_answer


def calc_game(username: str):
    print("What is the result of the expression?")

    # First iteration
    first_value, second_value = random.randint(1, 30), random.randint(1, 30)
    correct_answer = first_value + second_value

    print(f"Question: {first_value} + {second_value}")
    user_answer = int_input_answer()

    if not check_answer(
            user_answer=user_answer,
            correct_answer=correct_answer,
            username=username,
    ):
        return False

    # Second iteration
    first_value, second_value = random.randint(1, 30), random.randint(1, 30)
    correct_answer = max(first_value, second_value) - \
                     min(first_value, second_value)

    print(f"Question: {max(first_value, second_value)} - "
          f"{min(first_value, second_value)}")
    user_answer = int_input_answer()

    if not check_answer(
            user_answer=user_answer,
            correct_answer=correct_answer,
            username=username,
    ):
        return False

    # Third iteration
    first_value, second_value = random.randint(1, 10), random.randint(1, 10)
    correct_answer = first_value * second_value

    print(f"Question: {first_value} * {second_value}")
    user_answer = int_input_answer()

    if not check_answer(
            user_answer=user_answer,
            correct_answer=correct_answer,
            username=username,
    ):
        return False

    print(f"Congratulations, {username}!")
