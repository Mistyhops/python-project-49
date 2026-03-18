from brain_games.games.games import is_even_game
from brain_games.utils import welcome_script


def main():
    username = welcome_script()

    for _ in range(3):
        result = is_even_game(username=username)
        if not result:
            break
    else:
        print(f"Congratulations, {username}")


if __name__ == '__main__':
    main()
