from brain_games.games.games import is_prime_game
from brain_games.utils import welcome_script


def main():
    username = welcome_script()

    is_prime_game(username=username)


if __name__ == '__main__':
    main()
