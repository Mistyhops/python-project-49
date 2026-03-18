def welcome_script() -> str:
    welcome_message = f"Welcome to the Brain Games!"
    print(welcome_message)

    name_input_message = f"May I have your name? "
    username = input(name_input_message)

    print(f"Hello, {username}")

    return username


def check_answer(user_answer, correct_answer, username):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {username}!")
        return False


def int_input_answer() -> int:
    try:
        user_answer = int(input("Your answer: "))
    except ValueError as exc:
        print("Incorrect format answer. Enter integer")
        user_answer = int_input_answer()
    return user_answer
