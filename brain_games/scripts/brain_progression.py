from brain_games.games.games import progression_game
from brain_games.utils import welcome_script


def main():
    username = welcome_script()

    progression_game(username=username)


if __name__ == '__main__':
    main()
