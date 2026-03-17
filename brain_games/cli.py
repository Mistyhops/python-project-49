import prompt


def welcome_user():
    welcome_message = "Welcome to the Brain Games!"
    print(welcome_message)

    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
