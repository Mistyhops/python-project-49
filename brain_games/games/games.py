import random

import prompt

from brain_games.utils import int_input_answer, check_answer, make_progression


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
    correct_answer = max(first_value, second_value) - min(first_value, second_value)

    print(f"Question: {max(first_value, second_value)} - {min(first_value, second_value)}")
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

    print(f"Congratulations, {username}")


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
        print(f"Congratulations, {username}")


def progression_game(username: str):
    print("What number is missing in the progression?")

    for _ in range(3):
        progression = make_progression()
        random_position = random.randint(2, 6)

        correct_answer = progression[random_position]
        progression = [str(i) for i in progression]
        progression[random_position] = '..'
        progression = ' '.join(progression)

        print(f"Question: {progression}")

        user_answer = int_input_answer()

        if not check_answer(
                user_answer=user_answer,
                correct_answer=correct_answer,
                username=username,
        ):
            break
    else:
        print(f"Congratulations, {username}")
