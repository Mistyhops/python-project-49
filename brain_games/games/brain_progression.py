import random

from brain_games.utils import make_progression, int_input_answer, check_answer


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
        print(f"Congratulations, {username}!")
